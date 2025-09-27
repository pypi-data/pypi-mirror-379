from abc import ABC, abstractmethod
import re
import logging
import pandas as pd
from ollama import Client
from openai import OpenAI
from openai.types.responses.response_reasoning_item import ResponseReasoningItem
import google.generativeai as genai
from portkey_ai import Portkey
import typing_extensions as typing
from pydantic import BaseModel
import os
import json
from data_gatherer.prompts.prompt_manager import PromptManager
import tiktoken
from data_gatherer.resources_loader import load_config
from data_gatherer.retriever.embeddings_retriever import EmbeddingsRetriever
from data_gatherer.env import PORTKEY_GATEWAY_URL, PORTKEY_API_KEY, PORTKEY_ROUTE, PORTKEY_CONFIG, NYU_LLM_API, \
    GPT_API_KEY, GEMINI_KEY, DATA_GATHERER_USER_NAME
import requests
from json_repair import repair_json

from data_gatherer.llm.llm_client import LLMClient_dev
from data_gatherer.llm.response_schema import *

# Abstract base class for parsing data
class LLMParser(ABC):
    """
    This class is responsible for parsing data using LLMs. This will be done either:

    - Full Document Read (LLMs that can read the entire document)

    - Retrieve Then Read (LLMs will only read a target section retrieved from the document)
    """

    def __init__(self, open_data_repos_ontology, logger, log_file_override=None, full_document_read=True,
                 prompt_dir="data_gatherer/prompts/prompt_templates",
                 llm_name=None, save_dynamic_prompts=False, save_responses_to_cache=False, use_cached_responses=False,
                 use_portkey_for_gemini=True):
        """
        Initialize the LLMParser with configuration, logger, and optional log file override.

        :param open_data_repos_ontology: Configuration dictionary containing repo info

        :param logger: Logger instance for logging messages.

        :param log_file_override: Optional log file override.
        """
        self.open_data_repos_ontology = load_config(open_data_repos_ontology)

        self.logger = logger
        self.logger.info("LLMParser initialized.")

        self.llm_name = llm_name
        entire_document_models = ["gemini-1.5-flash", "gemini-1.5-pro", "gemini-2.0-flash-exp", "gemini-2.0-flash",
                                  "gemini-2.5-flash", "gpt-4o", "gpt-4o-mini", "gpt-5-nano", "gpt-5-mini", "gpt-5"]

        self.full_document_read = full_document_read and self.llm_name in entire_document_models
        self.title = None
        self.prompt_manager = PromptManager(prompt_dir, self.logger,
                                            save_dynamic_prompts=save_dynamic_prompts,
                                            save_responses_to_cache=save_responses_to_cache,
                                            use_cached_responses=use_cached_responses)
        self.repo_names = self.get_all_repo_names()
        self.repo_domain_to_name_mapping = self.get_repo_domain_to_name_mapping()

        self.save_dynamic_prompts = save_dynamic_prompts
        self.save_responses_to_cache = save_responses_to_cache
        self.use_cached_responses = use_cached_responses

        self.use_portkey_for_gemini = use_portkey_for_gemini

        if self.use_portkey_for_gemini and 'gemini' in llm_name:
            self.portkey = Portkey(
                api_key=PORTKEY_API_KEY,
                virtual_key=PORTKEY_ROUTE,
                base_url=PORTKEY_GATEWAY_URL,
                config=PORTKEY_CONFIG,
                metadata={"_user": DATA_GATHERER_USER_NAME}
            )

        elif llm_name == 'gemma3:1b':
            self.client = LLMClient_dev(model='gemma3:1b', logger=self.logger)

        elif llm_name == 'gemma3:4b':
            self.client = LLMClient_dev(model='gemma3:4b', logger=self.logger)

        elif llm_name == 'qwen:4b':
            self.client = LLMClient_dev(model='qwen:4b', logger=self.logger)

        elif llm_name == 'gemma2:9b':
            self.client = Client(host=NYU_LLM_API)  # env variable

        elif llm_name == 'gpt-4o-mini':
            self.client = OpenAI(api_key=GPT_API_KEY)

        elif llm_name == 'gpt-4o':
            self.client = OpenAI(api_key=GPT_API_KEY)

        elif llm_name == 'gpt-5-nano':
            self.client = OpenAI(api_key=GPT_API_KEY)

        elif llm_name == 'gpt-5-mini':
            self.client = OpenAI(api_key=GPT_API_KEY)

        elif llm_name == 'gpt-5':
            self.client = OpenAI(api_key=GPT_API_KEY)

        elif 'gemini' in llm_name:
            if not self.use_portkey_for_gemini:
                genai.configure(api_key=GEMINI_KEY)
                self.client = genai.GenerativeModel(llm_name)
            else:
                self.client = None

        else:
            raise ValueError(f"Unsupported LLM model: {llm_name}. Supported models are: "
                             f"{', '.join(entire_document_models)} and 'gemma2:9b'.")

    # create abstract method for subclasses to implement parse_data
    @abstractmethod
    def parse_data(self, raw_data, current_url):
        """
        Parse the raw data using the configured LLM.

        :param raw_data: The raw data to be parsed (XML or HTML).

        :param current_url: The current URL address being processed.

        :return: Parsed data as a DataFrame or list of dictionaries.
        """
        pass

    def extract_file_extension(self, download_link):
        self.logger.debug(f"Function_call: extract_file_extension({download_link})")
        # Extract the file extension from the download link
        extension = None
        if type(download_link) == str:
            extension = download_link.split('.')[-1]
        if type(extension) == str and ("/" in extension):  # or "?" in extension
            return ""
        return extension

    def load_patterns_for_tgt_section(self, section_name):
        """
        Load the XML tag patterns for the target section from the configuration.

        :param section_name: str — name of the section to load.

        :return: str — XML tag patterns for the target section.
        """

        self.logger.info(f"Function_call: load_patterns_for_tgt_section({section_name})")
        self.logger.info(f"Consider migrating this function to the BaseRetriever class.")
        return self.retriever.load_target_sections_ptrs(section_name)

    def generate_dataset_description(self, data_file):
        # from data file
        # excel, csv, json, xml, etc.
        # autoDDG
        raise NotImplementedError("DDG not implemented yet")

    def reconstruct_download_link(self, href, content_type, current_url_address):
        download_link = None
        self.logger.debug(f"Function_call: reconstruct_download_link({href}, {content_type}, {current_url_address})")
        if self.publisher == 'PMC':
            PMCID = re.search(r'PMC(\d+)', current_url_address, re.IGNORECASE).group(1)
            self.logger.debug(
                f"Inputs to reconstruct_download_link: {href}, {content_type}, {current_url_address}, {PMCID}")
            if content_type == 'local-data':
                download_link = "https://pmc.ncbi.nlm.nih.gov/articles/instance/" + PMCID + '/bin/' + href
            elif content_type == 'media p':
                file_name = os.path.basename(href)
                self.logger.debug(f"Extracted file name: {file_name} from href: {href}")
                download_link = "https://www.ncbi.nlm.nih.gov/pmc" + href

        else:
            self.logger.debug(f"Extracted download_link as href: {href}")
            download_link = href

        return download_link

    def union_additional_data(self, parsed_data, additional_data):
        self.logger.info(f"Merging additional data ({type(additional_data)}) with parsed data({type(parsed_data)}).")
        self.logger.info(f"Additional data\n{additional_data}")
        return pd.concat([parsed_data, additional_data], ignore_index=True)

    def process_additional_data(self, additional_data, prompt_name='retrieve_datasets_simple_JSON',
                                response_format=dataset_response_schema_gpt):
        """
        Process the additional data from the webpage. This is the data matched from the HTML with the patterns in
        retrieval_patterns xpaths.

        :param additional_data: List of dictionaries containing additional data to be processed.

        :return: List of dictionaries containing processed data.

        """
        self.logger.info(f"Processing additional data: {len(additional_data)} items")
        repos_elements = []
        for repo, details in self.open_data_repos_ontology['repos'].items():
            entry = repo
            if 'repo_name' in details:
                entry += f" ({details['repo_name']})"
            repos_elements.append(entry)

        # Join the elements into a properly formatted string
        repos = ', '.join(repos_elements)

        # Log for debugging
        self.logger.info(f"Repos elements: {repos_elements}")

        ret = []
        for element in additional_data:
            self.logger.info(f"Processing additional data element ({type(element)}): {element}")
            cont = element['surrounding_text']

            if 'Supplementary Material' in cont or 'supplementary material' in cont:
                continue

            if (element['source_section'] in ['data availability', 'data_availability', 'data_availability_elements']
                or 'data availability' in cont) and len(cont) > 1:
                self.logger.info(f"Processing data availability text")
                # Call the generalized function
                datasets = self.extract_datasets_info_from_content(
                    cont, 
                    repos_elements, model=self.llm_name,
                    temperature=0,
                    prompt_name=prompt_name,
                    response_format=response_format
                )

                for dt in datasets:
                    dt['source_section'] = element['source_section']
                    dt['retrieval_pattern'] = element['retrieval_pattern']

                ret.extend(datasets)
            else:
                self.logger.debug(f"Processing supplementary material element")
                ret.append(element)

        self.logger.info(f"Final ret additional data: {len(ret)} items")
        self.logger.debug(f"Final ret additional data: {ret}")
        return ret

    def process_data_availability_text(self, DAS_content, prompt_name='retrieve_datasets_simple_JSON',
                                       response_format=dataset_response_schema_gpt):
        """
        Process the data availability section from the webpage.

        :param DAS_content: list of all text content matching the data availability section patterns.

        :return: List of dictionaries containing processed data.
        """
        self.logger.info(f"Processing DAS_content: {len(DAS_content)} elements")
        repos_elements = self.repo_names

        # Call the generalized function
        datasets = []
        for element in DAS_content:
            datasets.extend(self.extract_datasets_info_from_content(element, repos_elements,
                                                                    model=self.llm_name,
                                                                    temperature=0,
                                                                    prompt_name=prompt_name,
                                                                    response_format=response_format))

        # Add source_section information and return
        ret = []
        self.logger.info(f"datasets ({type(datasets)}): {datasets}")
        for dataset in datasets:
            self.logger.info(f"iter dataset ({type(dataset)}): {dataset}")
            dataset['source_section'] = 'data_availability'
            self.logger.warning(f"Adding retrieval pattern 'data availability' to dataset")
            dataset['retrieval_pattern'] = 'data availability'
            ret.append(dataset)

        self.logger.info(f"Final ret data availability: {len(ret)} items")
        self.logger.info(f"Final ret data availability: {ret}")
        return ret

    def extract_datasets_info_from_content(self, content: str, repos: list, model: str = 'gpt-4o-mini',
                                           temperature: float = 0.0,
                                           prompt_name: str = 'retrieve_datasets_simple_JSON',
                                           full_document_read=True,
                                           response_format = dataset_response_schema_gpt) -> list:
        """
        Extract datasets from the given content using a specified LLM model.
        Uses a static prompt template and dynamically injects the required content.
        It also performs token counting and llm response normalization.

        :param content: The content to be processed.

        :param repos: List of repositories to be included in the prompt.

        :param model: The LLM model to be used for processing.

        :param temperature: The temperature setting for the model.

        :return: List of datasets retrieved from the content.
        """
        self.logger.info(f"Function_call: extract_datasets_info_from_content(...)")
        self.logger.debug(f"Loading prompt: {prompt_name} for model {model}")
        static_prompt = self.prompt_manager.load_prompt(prompt_name)
        n_tokens_static_prompt = self.count_tokens(static_prompt, model)

        if 'gpt' in model:
            while self.tokens_over_limit(content, model, allowance_static_prompt=n_tokens_static_prompt):
                content = content[:-2000]
        self.logger.info(f"Content length: {len(content)}")

        if 'gemma' in model or 'qwen' in model:
            if self.tokens_over_limit(content, model, allowance_static_prompt=n_tokens_static_prompt, limit=32000):
                self.logger.warning(f"Content length {len(content)} exceeds the model's token limit. "
                                    f"Truncating content to fit within the limit.")
                content = content[:-2000]

        self.logger.debug(f"static_prompt: {static_prompt}")

        # Render the prompt with dynamic content
        messages = self.prompt_manager.render_prompt(
            static_prompt,
            entire_doc=self.full_document_read,
            content=content,
            repos=', '.join(repos)
        )
        self.logger.info(f"Prompt messages total length: {self.count_tokens(messages, model)} tokens")
        self.logger.debug(f"Prompt messages: {messages}")

        # Generate the checksum for the prompt content
        # Save the prompt and calculate checksum
        prompt_id = f"{model}-{temperature}-{self.prompt_manager._calculate_checksum(str(messages))}"
        self.logger.info(f"Prompt ID: {prompt_id}")
        # Save the prompt using the PromptManager
        if self.save_dynamic_prompts:
            self.prompt_manager.save_prompt(prompt_id=prompt_id, prompt_content=messages)

        if self.use_cached_responses:
            # Check if the response exists
            cached_response = self.prompt_manager.retrieve_response(prompt_id)

        if self.use_cached_responses and cached_response:
            self.logger.info(f"Using cached response {type(cached_response)} from model: {model}")
            if type(cached_response) == str and 'gpt' in model:
                resps = [json.loads(cached_response)]
            if type(cached_response) == str:
                resps = cached_response.split("\n")
            elif type(cached_response) == list:
                resps = cached_response
        else:
            # Make the request to the model
            self.logger.info(
                f"Requesting datasets from content using model: {model}, temperature: {temperature}, messages length: "
                f"{self.count_tokens(messages, model)} tokens, schema: {response_format}")
            resps = []

            if model == 'gemma2:9b':
                response = self.client.chat(model=model, options={"temperature": temperature}, messages=messages)
                self.logger.info(
                    f"Response received from model: {response.get('message', {}).get('content', 'No content')}")
                resps = response['message']['content'].split("\n")
                # Save the response
                self.prompt_manager.save_response(prompt_id, response['message'][
                    'content']) if self.save_responses_to_cache else None
                self.logger.info(f"Response saved to cache")

            elif model == 'gemma3:1b' or model == 'gemma3:4b' or model == 'qwen:4b':
                response = self.client.api_call(messages, response_format=response_format.model_json_schema())
                parsed_resp = self.safe_parse_json(response)
                candidates = parsed_resp['datasets'] if isinstance(parsed_resp, dict) and 'datasets' in parsed_resp else parsed_resp
                if candidates:
                    self.logger.info(f"Found {len(candidates)} candidates in the response. Type {type(candidates)}")
                    if self.save_responses_to_cache:
                        self.prompt_manager.save_response(prompt_id, candidates)
                        self.logger.info(f"Response saved to cache")
                    parsed_response_dedup = self.normalize_response_type(candidates)
                    resps = parsed_response_dedup
                else:
                    self.logger.error("No candidates found in the response.")

            elif 'gpt' in model:
                response = None
                if 'gpt-5' in model:
                    if self.full_document_read:
                        response = self.client.responses.create(
                            model=model,
                            input=messages,
                            text={
                                "format": response_format
                            }
                        )
                    else:
                        response = self.client.responses.create(
                            model=model, 
                            input=messages,
                        )

                elif 'gpt-4o' in model: 
                    if self.full_document_read:
                        response = self.client.responses.create(
                            model=model,
                            input=messages,
                            temperature=temperature,
                            text={
                                "format": response_format
                            }
                        )
                    else:
                        response = self.client.responses.create(
                            model=model, 
                            input=messages,
                            temperature=temperature
                        )

                self.logger.info(f"GPT response: {response.output}")

                if self.full_document_read:
                    resps = self.safe_parse_json(response.output)  # 'datasets' keyError?
                    self.logger.info(f"Response is {type(resps)}: {resps}")
                    resps = resps.get("datasets", []) if resps is not None else []
                    resps = self.normalize_response_type(resps)
                    self.logger.info(f"Response is {type(resps)}: {resps}")
                    self.prompt_manager.save_response(prompt_id, resps) if self.save_responses_to_cache else None
                else:
                    try:
                        resps = self.safe_parse_json(response.output)  # Ensure it's properly parsed
                        resps = self.normalize_response_type(resps)
                        self.logger.info(f"Response is {type(resps)}: {resps}")
                        if not isinstance(resps, list):  # Ensure it's a list
                            raise ValueError("Expected a list of datasets, but got something else.")

                    except json.JSONDecodeError as e:
                        self.logger.error(f"JSON decoding error: {e}")
                        resps = []

                    self.prompt_manager.save_response(prompt_id, resps) if self.save_responses_to_cache else None

                # Save the response
                self.logger.info(f"Response {type(resps)} saved to cache") if self.save_responses_to_cache else None

            elif 'gemini' in model:
                if self.use_portkey_for_gemini:
                    # --- Portkey Gemini call ---
                    portkey_payload = {
                        "model": model,
                        "messages": messages,
                        "temperature": temperature,
                    }
                    try:
                        response = self.portkey.chat.completions.create(
                            **portkey_payload
                        )
                        self.logger.info(f"Portkey Gemini response: {response}")
                        if self.full_document_read:
                            resps = self.safe_parse_json(response)
                            resps = self.normalize_response_type(resps)
                            if isinstance(resps, dict):
                                resps = resps.get("datasets", []) if resps is not None else []
                        else:
                            try:
                                resps = self.safe_parse_json(response)
                                resps = self.normalize_response_type(resps)
                                if not isinstance(resps, list):
                                    raise ValueError("Expected a list of datasets, but got something else.")
                            except json.JSONDecodeError as e:
                                self.logger.error(f"JSON decoding error: {e}")
                                resps = []
                        # Save response if needed
                        if self.save_responses_to_cache:
                            self.prompt_manager.save_response(prompt_id, resps)
                    except Exception as e:
                        self.logger.error(f"Portkey Gemini call failed: {e}")
                        resps = []
                else:
                    if 'gemini' in model and 'flash' in model:
                        response = self.client.generate_content(
                            messages,
                            generation_config=genai.GenerationConfig(
                                response_mime_type="application/json",
                                response_schema=list[Dataset]
                            )
                        )
                        self.logger.debug(f"Gemini response: {response}")

                    elif model == 'gemini-1.5-pro':
                        response = self.client.generate_content(
                            messages,
                            request_options={"timeout": 1200},
                            generation_config=genai.GenerationConfig(
                                response_mime_type="application/json",
                                response_schema=list[Dataset]
                            )
                        )
                        self.logger.debug(f"Gemini Pro response: {response}")

                    try:
                        candidates = response.candidates  # Get the list of candidates
                        if candidates:
                            self.logger.info(f"Found {len(candidates)} candidates in the response.")
                            response_text = candidates[0].content.parts[0].text  # Access the first part's text
                            self.logger.info(f"Gemini response text: {response_text}")
                            parsed_response = json.loads(response_text)  # Parse the JSON response
                            if self.save_responses_to_cache:
                                self.prompt_manager.save_response(prompt_id, parsed_response)
                                self.logger.info(f"Response saved to cache")
                            parsed_response_dedup = self.normalize_response_type(parsed_response)
                            resps = parsed_response_dedup
                        else:
                            self.logger.error("No candidates found in the response.")
                    except Exception as e:
                        self.logger.error(f"Error processing Gemini response: {e}")
                        return None
            else:
                raise ValueError(f"Unsupported model: {model}. Please use a supported LLM model.")

        #if not self.full_document_read:
        #    return resps

        # Process the response content
        result = []
        for dataset in resps:
            self.logger.info(f"Processing dataset: {dataset}")
            if type(dataset) == str:
                self.logger.info(f"Dataset is a string")
                # Skip short or invalid responses
                if len(dataset) < 3 or dataset.split(",")[0].strip() == 'n/a' and dataset.split(",")[
                    1].strip() == 'n/a':
                    continue
                if len(dataset.split(",")) < 2:
                    continue
                if re.match(r'\*\s+\*\*[\s\w]+:\*\*', dataset):
                    dataset = re.sub(r'\*\s+\*\*[\s\w]+:\*\*', '', dataset)

                dataset_id, data_repository = [x.strip() for x in dataset.split(",")[:2]]

            elif type(dataset) == dict:
                self.logger.info(f"Dataset is a dictionary")

                dataset_id, data_repository, dataset_webpage = self.schema_validation(dataset)

            if (dataset_id is None or data_repository is None) and dataset_webpage is None:
                self.logger.info(f"Skipping dataset due to missing ID, repository, dataset page: {dataset}")
                continue

            if (dataset_id == 'n/a' or data_repository =='n/a') and dataset_webpage == 'n/a':
                self.logger.info(f"Skipping dataset due to missing ID, repository, dataset page: {dataset}")
                continue

            result.append({
                "dataset_identifier": dataset_id,
                "data_repository": data_repository,
                "dataset_webpage": dataset_webpage if dataset_webpage is not None else 'n/a',
                "citation_type": dataset.get('citation_type', 'n/a')
            })

            if 'decision_rationale' in dataset:
                result[-1]['decision_rationale'] = dataset['decision_rationale']

            if 'dataset-publication_relationship' in dataset:
                result[-1]['dataset-publication_relationship'] = dataset['dataset-publication_relationship']

            self.logger.info(f"Extracted dataset: {result[-1]}")

        self.logger.debug(f"Final result: {result}")

        return result

    def schema_validation(self, dataset):
        """
        Validate and extract dataset information based on the schema.

        :param dataset: dict — dataset information to be validated.

        :return: tuple — (dataset_id, data_repository, dataset_webpage) or (None, None, None) if invalid.
        """
        dataset_id, data_repository, dataset_webpage = None, None, None

        for repo_key, repo_vals in self.open_data_repos_ontology['repos'].items():
            for key, val in dataset.items():
                if 'dataset_webpage_url_ptr' in repo_vals:
                    ptr_search = re.sub('__ID__', '', repo_vals['dataset_webpage_url_ptr'])
                    if re.search(ptr_search, val, re.IGNORECASE):
                        self.logger.info(f"Matched dataset_webpage_url_ptr: {repo_vals['dataset_webpage_url_ptr']} to value: {val}")
                        if dataset_webpage is None:
                            self.logger.info(f"Candidate dataset_webpage: {val}")
                            dataset_webpage = val
                        if data_repository is None:
                            self.logger.info(f"Candidate data_repository: {repo_key}")
                            data_repository = self.resolve_data_repository(dataset.get('data_repository',
                                                                        dataset.get('repository_reference', 'n/a')),
                                                           identifier=dataset.get('dataset_identifier', dataset.get('dataset_id', 'n/a')),
                                                           dataset_page=dataset_webpage,
                                                           candidate_repo=repo_key)
                                                           
                if 'id_pattern' in repo_vals:
                    if re.search(repo_vals['id_pattern'], val, re.IGNORECASE):
                        self.logger.info(f"Matched id_pattern: {repo_vals['id_pattern']} to value: {val}")
                        if val.startswith('http'):
                            if dataset_webpage is None:
                                self.logger.info(f"Setting dataset_webpage to value: {val}")
                                dataset_webpage = val
                            ptr_sub = f'\b({repo_vals["id_pattern"]})'
                            self.logger.info(f"Using id_pattern to extract ID: {ptr_sub}")
                            match = re.search(ptr_sub, val, re.IGNORECASE)
                            if match and dataset_id is None:
                                self.logger.info(f"Setting dataset_id to value: {match.group(1)}")
                                dataset_id = match.group(1)
                            self.logger.info(f"Extracted ID: {dataset_id}")
                        else:
                            if (val.startswith('10.') or val.startswith('doi:10.')) and dataset_webpage is None:
                                self.logger.info(f"Setting dataset_webpage to DOI URL value: https://doi.org/{val}")
                                dataset_webpage = f"https://doi.org/{val}"
                                dataset_id = val
                            if dataset_id is None:
                                self.logger.info(f"Setting dataset_id to value: {val}")
                                dataset_id = val
                            if data_repository is None:
                                self.logger.info(f"Candidate data_repository: {repo_key}")
                                data_repository = self.resolve_data_repository(dataset.get('data_repository',
                                                                        dataset.get('repository_reference', 'n/a')),
                                                           identifier=dataset.get('dataset_identifier', dataset.get('dataset_id', 'n/a')),
                                                           dataset_page=dataset_webpage,
                                                           candidate_repo=repo_key)

        self.logger.info(f"Schema validation vals: {dataset_id}, {data_repository}, {dataset_webpage}")

        if dataset_id is None:
            dataset_id = self.validate_dataset_id(dataset.get('dataset_identifier', dataset.get('dataset_id', 'n/a')))
        else:
            self.logger.info(f"Dataset ID found via pattern matching: {dataset_id}")

        if data_repository is None:
            data_repository = self.resolve_data_repository(dataset.get('data_repository',
                                                                        dataset.get('repository_reference', 'n/a')),
                                                           identifier=dataset_id,
                                                           dataset_page=dataset_webpage)
        else:
            self.logger.info(f"Data repository found via pattern matching: {data_repository}")

        if dataset_webpage is None and 'dataset_webpage' in dataset:
            dataset_webpage = self.validate_dataset_webpage(dataset['dataset_webpage'], data_repository,
                                                            dataset_id, dataset)
        elif dataset_webpage is None:
            self.logger.info(f"Dataset webpage not extracted")
        else:
            self.logger.info(f"Dataset webpage found via pattern matching: {dataset_webpage}")
            dataset_webpage = self.validate_dataset_webpage(dataset_webpage, data_repository,
                                                            dataset_id, dataset)
        self.logger.info(f"Final schema validation vals: {dataset_id}, {data_repository}, {dataset_webpage}")

        if dataset_id == 'n/a' and data_repository in self.open_data_repos_ontology['repos']:
            self.logger.info(f"Dataset ID is 'n/a' and repository name from prompt")
            return None, None, None

        elif data_repository == 'n/a' and dataset_webpage == 'n/a':
            self.logger.info(f"Data repository is 'n/a', skipping dataset")
            return None, None, None

        return dataset_id, data_repository, dataset_webpage

    def normalize_response_type(self, response):
        """
        This function handles basic **postprocessing** of the LLM output.
        Normalize and deduplicate dataset responses by stripping DOI-style prefixes
        like '10.x/' from dataset IDs and keeping only one entry per PXD.

        :param response: List of dataset responses to be deduplicated (LLM Output).

        :return: List of deduplicated dataset responses.

        """
        self.logger.info(f"Deduplicating response with {len(response)} items")
        seen = set()
        deduped = []

        if not isinstance(response, list) and isinstance(response, dict):
            response = [response]

        for item in response:
            self.logger.debug(f"Processing item: {item}")
            dataset_id = item.get("dataset_identifier", item.get("dataset_id", ""))
            if not dataset_id:
                self.logger.warning(f"Skipping item with missing dataset_id: {item}")
                continue
            repo = item.get("data_repository", item.get("repository_reference", "n/a"))

            # Normalize: remove DOI prefix if it matches '10.x/PXD123456'
            clean_id = re.sub(r'10\.\d+/(\bPXD\d+\b)', r'\1', dataset_id)

            if clean_id not in seen:
                # Update the dataset_id to the normalized version
                item["dataset_id"] = clean_id
                self.logger.info(f"Adding unique item: {clean_id}")
                deduped.append(item)
                seen.add(clean_id)

            elif clean_id == 'n/a' and repo != 'n/a':
                deduped.append(item)

            else:
                self.logger.info(f"Duplicate found and skipped: {clean_id}")

        return deduped

    def safe_parse_json(self, response_text):
        """
        Cleans and safely parses JSON from an LLM response, fixing common issues.

        :param response_text: str or dict — the JSON string or Portkey response object to be parsed.

        :return: dict or None — parsed JSON object or None if parsing fails.
        """
        # Handle Portkey Gemini response object or OpenAI-like object
        self.logger.info(f"Function_call: safe_parse_json(response_text {type(response_text)})")
        # Accept both dict and objects with .choices attribute
        if hasattr(response_text, "choices"):
            # Likely an OpenAI/Portkey object, extract content
            try:
                response_text = response_text.choices[0].message.content
                self.logger.debug(f"Extracted content from response object, type: {type(response_text)}")
            except Exception as e:
                self.logger.warning(f"Could not extract content from response object: {e}")
                return None
        elif isinstance(response_text, list):
            self.logger.info(f"Response is a list of length: {len(response_text)}")
            for response_item in response_text:
                self.logger.info(f"List item type: {type(response_item)}")
                if hasattr(response_item, "content"):
                    self.logger.info(f"Item has content attribute, of type: {type(response_item.content)}")
                    if isinstance(response_item.content, list) and len(response_item.content) > 0:
                        response_text = response_item.content[0].text
                else:
                    response_text = str(response_item)
        elif isinstance(response_text, dict):
            try:
                response_text = response_text["choices"][0]["message"]["content"]
            except Exception as e:
                self.logger.warning(f"Could not extract content from response dict: {e}")
                return None

        response_text = response_text.strip()

        # Remove markdown formatting
        if response_text.startswith("```"):
            response_text = re.sub(r"^```[a-zA-Z]*\n?", "", response_text)
            response_text = re.sub(r"\n?```$", "", response_text)
        
        self.logger.debug(f"Cleaned response text for JSON parsing: {response_text[:500]}")

        try:
            # First try standard parsing
            return json.loads(response_text)
        except json.JSONDecodeError:
            self.logger.warning("Initial JSON parsing failed. Attempting json_repair...")

            try:
                repaired = repair_json(response_text)
                repaired = re.sub(r',\s*\{\}\]', ']', repaired)  # Remove trailing empty objects in lists
                return json.loads(repaired)
            except Exception as e:
                self.logger.warning(f"json_repair failed: {e}")
                self.logger.info(f"Malformed JSON (after attempted repair): {repaired[:500]}")
                return None

    def process_data_availability_links(self, dataset_links):
        """
        Given the link, the article title, and the text around the link, create a column (identifier),
        and a column for the dataset.

        :param dataset_links: List of dictionaries containing href links and their context.

        :return: List of dictionaries containing processed dataset information.

        """
        self.logger.info(f"Analyzing data availability statement with {len(dataset_links)} links")
        self.logger.debug(f"Text from data-availability: {dataset_links}")

        model = self.llm_name
        temperature = 0.0

        ret = []
        progress = 0

        for link in dataset_links:
            self.logger.info(f"Processing link: {link['href']}")

            if progress > len(dataset_links):
                break

            ret_element = {}

            # Detect if the link is already a dataset webpage
            detected = self.dataset_webpage_url_check(link['href'])
            if detected is not None:
                self.logger.info(f"Link {link['href']} points to dataset webpage")
                ret.append(detected)
                progress += 1
                continue

            # Prepare the dynamic prompt
            dynamic_content = {
                "href": link['href'],
                "surrounding_text": link['surrounding_text']
            }
            static_prompt = self.prompt_manager.load_prompt("retrieve_datasets_fromDAS")
            messages = self.prompt_manager.render_prompt(static_prompt, self.full_document_read, **dynamic_content)

            # Generate a unique checksum for the prompt
            prompt_id = f"{model}-{temperature}-{self.prompt_manager._calculate_checksum(str(messages))}"
            self.logger.info(f"Prompt ID: {prompt_id}")

            # Check if the response exists
            cached_response = self.prompt_manager.retrieve_response(prompt_id)
            if cached_response:
                self.logger.info("Using cached response.")
                resp = cached_response.split("\n")
            else:
                # Make the request to the LLM model
                self.logger.info(f"Requesting datasets using model: {model}, messages: {messages}")
                resp = []

                if model == 'gemma2:9b':
                    response = self.client.chat(model='gemma2:9b', options={"temperature": 0}, messages=messages)
                    self.logger.info(
                        f"Response received from gemma2:9b: {response.get('message', {}).get('content', 'No content')}")
                    resp = response['message']['content'].split("\n")
                    self.prompt_manager.save_response(prompt_id, response['message']['content'])
                    self.logger.info(f"Response saved to cache")

                elif 'gpt' in model:
                    if 'gpt-4o' in model:
                        response = self.client.responses.create(
                            model=model,
                            input=messages,
                            temperature=0
                        )
                    elif 'gpt-5' in model:
                        response = self.client.responses.create(
                            model=model,
                            input=messages,
                        )
                    self.logger.info(f"GPT response: {response.output}")
                    resp = response.output.split("\n")
                    self.prompt_manager.save_response(prompt_id, response.output)
                    self.logger.info(f"Response saved to cache")

            # Process the response
            ret_element['link'] = link['href']
            ret_element['content_type'] = 'data_link'

            if type(resp) == list:
                for r in resp:
                    append_item = ret_element.copy()
                    self.logger.info(f"Response: '{r}', len: {len(r)}")
                    # string that is less than 1 char + 1 comma + 1 char
                    if len(r) < 3:
                        continue
                    # skip strings that do not conform to expected output
                    if r.count(',') != 1:
                        continue
                    append_item['dataset_identifier'], append_item['data_repository'] = r.split(
                        ',')
                    append_item['dataset_identifier'] = append_item['dataset_identifier'].strip()
                    append_item['data_repository'] = append_item['data_repository'].strip()
                    append_item['source_section'] = link['source_section']
                    append_item['retrieval_pattern'] = link[
                        'retrieval_pattern'] if 'retrieval_pattern' in link.keys() else None
                    ret.append(append_item)
                    self.logger.info(f"Response appended to df {append_item}")
                    progress += 1
                self.logger.info(f"Updated ret: {ret}")
            else:
                self.logger.info(f"Response: '{resp}', len: {len(resp)}. Response appended to df")
                ret_element['dataset_identifier'], ret_element['data_repository'] = (
                    response['message']['content'].split(','))
                # trim leading and trailing whitespaces
                ret_element['dataset_identifier'] = ret_element['dataset_identifier'].strip()
                ret_element['data_repository'] = ret_element['data_repository'].strip()
                ret_element['source_section'] = link['source_section']
                ret_element['retrieval_pattern'] = link[
                    'retrieval_pattern'] if 'retrieval_pattern' in link.keys() else None
                ret.append(ret_element)
                progress += 1

        return ret

    def brute_force_dataset_webpage_url_check(self, url):
        """
        Iterate over all the known data repositories and check if the URL matches any of their dataset webpage patterns.
        """
        result = None
        self.logger.info(f"Brute-force checking if link points to dataset webpage: {url}")
        for repo in self.open_data_repos_ontology['repos'].keys():
            if 'dataset_webpage_url_ptr' in self.open_data_repos_ontology['repos'][repo]:
                pattern = self.open_data_repos_ontology['repos'][repo]['dataset_webpage_url_ptr']
                result = re.search(pattern, url, re.IGNORECASE)
            if result is not None:
                self.logger.info(f"Link {url} points to dataset webpage in repo {repo}")
                return url
        return None

    def dataset_webpage_url_check(self, url, resolved_repo=None):
        """
        Check if the URL directly points to a dataset webpage.

        :param url: str — the URL to be checked.

        :return: dict or None — dictionary with data repository information if one pattern from ontology matches that
        """
        ret = {}
        self.logger.info(f"Checking if link points to dataset webpage: {url}")
        repo = self.resolve_data_repository(url) if resolved_repo is None else resolved_repo
        self.logger.info(f"Extracted domain: {repo}")
        if (repo in self.open_data_repos_ontology['repos'].keys() and
                'dataset_webpage_url_ptr' in self.open_data_repos_ontology['repos'][repo].keys()):
            self.logger.info(f"Link {url} could point to dataset webpage")
            pattern = self.open_data_repos_ontology['repos'][repo]['dataset_webpage_url_ptr']
            self.logger.debug(f"Pattern: {pattern}")
            match = re.match(pattern, url)
            # if the link matches the pattern, extract the dataset identifier and the data repository
            if match:
                self.logger.info(f"Match with pattern: {pattern}")
                ret['data_repository'] = repo
                ret['dataset_identifier'] = match.group(1)
                ret['dataset_webpage'] = url
                ret['link'] = url
                return ret
            elif re.search(re.sub(pattern, '__ID__', '', re.IGNORECASE), url):
                self.logger.info(f"Link matches the pattern {pattern} with __ID__ replaced")
                extracted_id = 'n/a'
                ret['data_repository'] = repo
                if 'id_pattern' in self.open_data_repos_ontology['repos'][repo].keys():
                    ptr_sub = f'.*({self.open_data_repos_ontology["repos"][repo]["id_pattern"]}).*'
                    self.logger.info(f"Using id_pattern to extract ID: {ptr_sub}")
                    match = re.search(ptr_sub, url, re.IGNORECASE)
                    if match:
                        extracted_id = match.group(1)
                    self.logger.info(f"Extracted ID: {extracted_id}")
                ret['dataset_identifier'] = extracted_id
                ret['dataset_webpage'] = url
                ret['link'] = url
                return ret
            else:
                self.logger.info(f"Link does not match the pattern")
                return None

        return None

    def normalize_LLM_output(self, response):
        cont = response['message']['content']
        self.logger.info(f"Normalizing {type(cont)} LLM output: {cont}")
        output = cont.split(",")
        repo = re.sub(r"[\n\s]*", "", output.pop())
        self.logger.info(f"Repo: {repo}")
        ret = []
        for i in range(len(output)):
            ret.append(re.sub(r"\s*and\s+", " ", output[i]) + "," + repo)
        return ret

    def url_to_repo_domain(self, url, dataset_webpage_url=None):

        self.logger.info(f"Function call: url_to_repo_domain({url},{dataset_webpage_url})")

        if dataset_webpage_url is not None:
            url = dataset_webpage_url

        if url in self.open_data_repos_ontology['repos'].keys():
            return url

        self.logger.info(f"Extracting repo domain from URL: {url}")
        match = re.match(r'^https?://([\.\w\-]+)\/*', url)
        if match:
            domain = match.group(1)
            self.logger.debug(f"Repo Domain: {domain}")
            if (domain in self.open_data_repos_ontology['repos'].keys() and
                    'repo_mapping' in self.open_data_repos_ontology['repos'][domain].keys()):
                return self.open_data_repos_ontology['repos'][domain]['repo_mapping']
            return domain
        elif '.' not in url:
            return url
        elif ' ' not in url and '/' not in url:
            self.logger.warning(f"URL {url} may be a domain already.")
            return url
        else:
            self.logger.error(f"Error extracting domain from URL: {url}")
            return 'Unknown_Publisher'

    def get_all_repo_names(self, uncased=False):
        # Get the all the repository names from the config file. (all the repos in ontology)
        repo_names = []
        for k, v in self.open_data_repos_ontology['repos'].items():
            if 'repo_name' in v.keys():
                repo_names.append(v['repo_name'])
            else:
                repo_names.append(k)
        repo_names = [x.lower() for x in repo_names] if uncased else repo_names
        self.logger.debug(f"All repository names: {repo_names}")
        return repo_names

    def get_repo_domain_to_name_mapping(self):
        # Get the mapping of repository domains to names from ontology
        repo_mapping = {}
        for k, v in self.open_data_repos_ontology['repos'].items():
            if 'repo_name' in v.keys():
                repo_mapping[k] = v['repo_name'].lower()
            else:
                repo_mapping[k] = k

        ret = {v: k for k, v in repo_mapping.items()}
        self.logger.debug(f"Repo mapping: {ret}")
        return ret

    def validate_dataset_id(self, dataset_identifier):
        """
        This function checks for hallucinations, i.e. if the dataset identifier is a known repository name.
        """
        self.logger.info(f"Validating accession ID: {dataset_identifier}")
        if dataset_identifier.lower() in self.get_all_repo_names(uncased=True):
            self.logger.info(f"Accession ID {dataset_identifier} is a known repository --> invalid, returning 'n/a'")
            return 'n/a'
        elif ' ' in dataset_identifier or dataset_identifier == 'n/a' or len(dataset_identifier) < 3:
            self.logger.info(f"Accession ID {dataset_identifier} is invalid")
            return 'n/a'
        elif dataset_identifier.startswith('http') and 'doi.org' in dataset_identifier:
            dataset_identifier = re.sub(r'https?://doi\.org/', '', dataset_identifier, re.IGNORECASE)
            dataset_identifier = re.sub(r'doi:', '', dataset_identifier, re.IGNORECASE)
            return dataset_identifier
        elif dataset_identifier.startswith('http'):
            new_metadata = self.dataset_webpage_url_check(dataset_identifier)
            new_id = new_metadata['dataset_identifier'] if new_metadata is not None else 'n/a'
            self.logger.info(f"Accession ID {new_id} is valid") if new_id != 'n/a' else self.logger.info(
                f"Accession ID {dataset_identifier} is invalid")
            return new_id
        else:
            self.logger.info(f"Accession ID {dataset_identifier} is valid")
            return dataset_identifier

    def validate_dataset_webpage(self, dataset_webpage_url, resolved_repo, dataset_id, old_metadata=None):
        """
        This function checks for hallucinations, i.e. if the dataset identifier is a known repository name.
        Input:
        dataset_webpage_url: str - the URL to be validated
        resolved_repo: str - the resolved repository name
        dataset_id: str - the dataset identifier
        old_metadata: dict - the old metadata dictionary (optional)
        """
        self.logger.info(f"Validating Dataset Page: {dataset_webpage_url}, resolved_repo {resolved_repo}, dataset_id {dataset_id}")
        resolved_dataset_page = self.resolve_url(dataset_webpage_url)

        if resolved_repo in self.open_data_repos_ontology['repos']:
            if 'dataset_webpage_url_ptr' in self.open_data_repos_ontology['repos'][resolved_repo].keys():
                dataset_webpage_url_ptr = self.open_data_repos_ontology['repos'][resolved_repo]['dataset_webpage_url_ptr']
                pattern = re.sub(r'__ID__', '', dataset_webpage_url_ptr)
                self.logger.info(f"Pattern: {pattern}, resolved_dataset_page: {resolved_dataset_page}")
                if re.search(pattern, resolved_dataset_page, re.IGNORECASE) or pattern in resolved_dataset_page:
                    self.logger.info(f"Link matches the pattern {pattern} of resolved_dataset_page.")
                    return resolved_dataset_page
                else:
                    self.logger.info(f"Link does not match the pattern {pattern } of resolved_dataset_page.")
                    return 'n/a'
            else:
                self.logger.info(f"No dataset_webpage_url_ptr found for {resolved_repo}")
                return resolved_dataset_page
        elif dataset_id in resolved_dataset_page:
            self.logger.info(f"Dataset ID {dataset_id} found in resolved dataset page {resolved_dataset_page}")
            return resolved_dataset_page
        elif old_metadata is not None:
            for k,v in old_metadata.items():
                self.logger.info(f"Brute-force checking old metadata {k}: {v}")
                checked_url = self.brute_force_dataset_webpage_url_check(v)
                if checked_url is not None:
                    self.logger.info(f"Found valid dataset webpage in old metadata {k}: {checked_url}")
                    return checked_url

        self.logger.info(f"Repository {resolved_repo} not found in ontology")
        return 'n/a'

    def resolve_url(self, url):
        try:
            response = requests.get(url, allow_redirects=True, timeout=5)
            self.logger.info(f"Resolved URL: {response.url}")
            return response.url
        except requests.RequestException as e:
            self.logger.warning(f"Error resolving URL {url}: {e}")
            return url

    def resolve_accession_id_for_repository(self, dataset_identifier, data_repository, resolved_dataset_page=None):
        """
        This function resolves the accession ID for a given dataset identifier and data repository.
        It checks if the dataset identifier matches the expected pattern for the given repository (from ontology)
        """
        self.logger.info(f"Resolving accession ID for {dataset_identifier} in {data_repository}, resolved page: {resolved_dataset_page}")
        if data_repository in self.open_data_repos_ontology['repos']:
            repo_config = self.open_data_repos_ontology['repos'][data_repository]
            pattern = repo_config.get('id_pattern')
            if pattern and not re.match(pattern, dataset_identifier, re.IGNORECASE):
                self.logger.warning(f"Identifier {dataset_identifier} does not match pattern for {data_repository}")
            else:
                self.logger.warning(f"id_pattern not defined for {data_repository} in ontology. Add definition to improve validation.")

            if pattern and resolved_dataset_page is not None:
                self.logger.info(f"Extracting ID from dataset page {resolved_dataset_page} using pattern {pattern}")
                match = re.search(f"({pattern})", resolved_dataset_page, re.IGNORECASE)
                if match:
                    dataset_identifier = match.group(1)
                    self.logger.info(f"Extracted ID: {dataset_identifier}")

            if 'default_id_suffix' in repo_config and not dataset_identifier.endswith(repo_config['default_id_suffix']):
                return dataset_identifier.lower() + repo_config['default_id_suffix']

        else:
            self.logger.warning(f"Repository {data_repository} not found in ontology")
    
        return dataset_identifier

    def resolve_data_repository(self, repo: str, identifier=None, dataset_page=None, candidate_repo=None) -> str:
        """
        Normalize the repository domain from a URL or text reference using config mappings in ontology.

        :param repo: str — the repository name or URL to be normalized.

        :return: str — the normalized repository name.
        """
        self.logger.info(f"Resolving data repository for candidate: {repo}, identifier: {identifier}, dataset_page: {dataset_page}")

        if repo is None:
            self.logger.warning(f"Repository is None")
            return 'n/a'

        if ',' in repo and ',' in identifier:
            self.logger.warning(f"Repository contains a comma: {repo}. Same data may be in multiple repos.")
            ret = []
            for r in repo.split(','):
                r = r.strip()
                if r in self.open_data_repos_ontology['repos']:
                    ret.append(self.resolve_data_repository(r).lower())
            return ret

        if isinstance(repo, list):
            self.logger.warning(f"Repository is a list: {repo}. Same data may be in multiple repos.")
            ret = []
            for r in repo:
                r = r.strip()
                if r in self.open_data_repos_ontology['repos']:
                    ret.append(self.resolve_data_repository(r).lower())
            return ret

        if repo.startswith('http'):
            check_url = self.brute_force_dataset_webpage_url_check(repo)
            if check_url:
                self.logger.info(f"Repository {repo} is a dataset webpage {check_url}")
                return check_url

        resolved_to_known_repo = False

        for k, v in self.open_data_repos_ontology['repos'].items():
            self.logger.debug(f"Checking if {repo} == {k}. Repo vals: {v.keys()}")
            repo = re.sub(r"\(", " ", repo)
            repo = re.sub(r"\)", " ", repo)
            # match where repo_link has been extracted
            if k.lower() == repo.lower():
                self.logger.info(f"Exact - case insensitive - match found for repo: {repo}")
                resolved_to_known_repo = True
                repo = k
                break

            if not resolved_to_known_repo and 'repo_name' in v.keys():
                if repo.lower() == v['repo_name'].lower():
                    self.logger.info(f"Found repo_name match for {repo}")
                    repo = k
                    resolved_to_known_repo = True
                    break

                elif v['repo_name'].lower() in repo.lower():
                    self.logger.info(f"Found partial match for {repo} in {v['repo_name']}")
                    repo = k
                    resolved_to_known_repo = True
                    break

            if not resolved_to_known_repo and identifier is not None and identifier != 'n/a' and 'id_pattern' in v.keys():
                self.logger.info(f"Checking id_pattern {v['id_pattern']} match with identifier {identifier} for {repo}")
                if re.match(v['id_pattern'], identifier, re.IGNORECASE):
                    self.logger.info(f"Found id_pattern match for {repo} in {v['id_pattern']}")
                    repo = k
                    resolved_to_known_repo = True
                    break

        if not resolved_to_known_repo:
            repo = self.url_to_repo_domain(repo, dataset_page)
            self.logger.info(f"data_repository not resolved, using domain")

        if repo in self.open_data_repos_ontology['repos'] and 'repo_mapping' in self.open_data_repos_ontology['repos'][
            repo]:
            repo = self.open_data_repos_ontology['repos'][repo]['repo_mapping']
            self.logger.info(f"Resolved data repository: {repo}")
        
        if candidate_repo is not None and candidate_repo in self.open_data_repos_ontology['repos'] and \
            'repo_root' in self.open_data_repos_ontology['repos'][candidate_repo] and \
            self.open_data_repos_ontology['repos'][candidate_repo]['repo_root'] == repo:
            self.logger.info(f"Using candidate repo {candidate_repo} as it matches the resolved repo config.")
            return candidate_repo.lower()

        return repo.lower()  # fallback

    def get_dataset_page(self, datasets):
        """
        Given a list of dataset dictionaries, reconstruct the dataset page, by using navigation patterns
        from the ontology. The function will add a new key to the dataset dictionary with the webpage URL.

        :param datasets: list of dictionaries containing dataset information.

        :return: list of dictionaries with updated dataset information including dataset webpage URL.
        """
        if datasets is None:
            return None

        self.logger.info(f"Fetching metadata for {len(datasets)} datasets")

        for i, item in enumerate(datasets):

            if type(item) != dict:
                self.logger.error(f"can't resolve dataset_webpage for non-dict item {1 + i}: {item}")
                continue

            self.logger.info(f"Processing dataset {1 + i} with keys: {item.keys()}")

            if 'data_repository' not in item.keys() and 'repository_reference' not in item.keys():
                self.logger.info(f"Skipping dataset {1 + i}: no data_repository for item")
                continue

            accession_id = item.get('dataset_identifier', item.get('dataset_id', 'n/a'))
            if accession_id == 'n/a':
                self.logger.info(f"Skipping dataset {1 + i}: no dataset_identifier for item")
                continue
            else:
                self.logger.info(f"Raw accession ID: {accession_id}")

            if 'data_repository' in item.keys():
                original_repo = item['data_repository']
                repo = self.resolve_data_repository(original_repo, identifier=accession_id)
            elif 'repository_reference' in item.keys():
                original_repo = item['repository_reference']
                repo = self.resolve_data_repository(original_repo, identifier=accession_id)
            else:
                self.logger.error(f"Error extracting data repository for item: {item}")
                continue

            if isinstance(repo, list):
                if len(repo) > 0:
                    self.logger.info(f"Repository is a list: {repo}. Resolving accession ID for each element.")
                    repo = repo[0]
                else:
                    self.logger.warning("Repository list is empty. Skipping this dataset.")
                    continue  # or `return None`, depending on context

            dataset_page = item.get('dataset_webpage', item.get('dataset_page', None))

            accession_id = self.resolve_accession_id_for_repository(accession_id, repo, dataset_page)

            self.logger.info(f"Processing dataset {1 + i} with repo: {repo} and accession_id: {accession_id}")
            self.logger.debug(f"Processing dataset {1 + i} with keys: {item.keys()}")

            updated_dt = False

            if repo in self.open_data_repos_ontology['repos'].keys():

                if "dataset_webpage_url_ptr" in self.open_data_repos_ontology['repos'][repo]:
                    dataset_page_ptr = self.open_data_repos_ontology['repos'][repo]['dataset_webpage_url_ptr']
                    if dataset_page and re.search(dataset_page_ptr.replace('__ID__', ''), dataset_page, re.IGNORECASE):
                        self.logger.info(f"Dataset page {dataset_page} already matches pattern for {repo}")
                        dataset_webpage = dataset_page
                    else:
                        self.logger.info(f"Using pattern {dataset_page_ptr} to construct dataset page for {repo}")
                        dataset_webpage = re.sub('__ID__', accession_id, dataset_page_ptr)

                elif ('dataset_webpage' in item.keys()):
                    self.logger.debug(f"Skipping dataset {1 + i}: already has dataset_webpage")
                    continue

                else:
                    self.logger.warning(
                        f"No dataset_webpage_url_ptr found for {repo}. Maybe lost in refactoring 21 April 2025")
                    dataset_webpage = 'na'

                self.logger.info(f"Dataset page: {dataset_webpage}")
                datasets[i]['dataset_webpage'] = dataset_webpage

                # add access mode
                if 'access_mode' in self.open_data_repos_ontology['repos'][repo]:
                    access_mode = self.open_data_repos_ontology['repos'][repo]['access_mode']
                    datasets[i]['access_mode'] = access_mode
                    self.logger.info(f"Adding access mode for dataset {1 + i}: {access_mode}")

            elif original_repo.startswith('http'):
                datasets[i]['data_repository'] = repo
                datasets[i]['dataset_webpage'] = original_repo

            else:
                self.logger.warning(f"Repository {repo} unknown in Ontology. Skipping dataset page {1 + i}.")
                datasets[i]['dataset_webpage'] = 'n/a'
                continue

        self.logger.info(f"Updated datasets len: {len(datasets)}")
        return datasets

    def get_NuExtract_template(self):
        """
        template = '''{
                    "Available Dataset": {
                        "data repository name" = "",
                        "data repository link" = "",
                        "dataset identifier": "",
                        "dataset webpage": "",
            }
            }'''

            return template
            """
        raise NotImplementedError("This method should be implemented in a subclass.")

    def tokens_over_limit(self, html_cont: str, model="gpt-4", limit=128000, allowance_static_prompt=200):
        # Use tiktoken only for OpenAI models, fallback to rough estimate for others
        if 'gpt-4' in model:
            encoding = tiktoken.encoding_for_model(model)
            tokens = encoding.encode(html_cont)
            self.logger.info(f"Number of tokens: {len(tokens)}")
            return len(tokens) + int(allowance_static_prompt * 1.25) > limit
        else:
            # Rough estimate: 1 token ≈ 4 characters
            n_tokens = len(html_cont) // 4
            self.logger.info(f"Estimated number of tokens for model '{model}': {n_tokens}")
            return n_tokens + int(allowance_static_prompt * 1.25) > limit

    def count_tokens(self, prompt, model="gpt-4o-mini") -> int:
        """
        Count the number of tokens in a given prompt for a specific model.

        :param prompt: str — the prompt to be tokenized.

        :param model: str — the model name (default: "gpt-4").

        :return: int — the number of tokens in the prompt.
        """
        n_tokens = 0

        # **Ensure `prompt` is a string**
        if isinstance(prompt, list):
            self.logger.info(f"Expected string but got list. Converting list to string.")
            prompt = " ".join([msg["content"] for msg in prompt if isinstance(msg, dict) and "content" in msg])

        elif not isinstance(prompt, str):
            self.logger.error(f"Unexpected type for prompt: {type(prompt)}. Converting to string.")
            prompt = str(prompt)

        self.logger.debug(f"Counting tokens for model: {model}, prompt length: {len(prompt)} char")
        # **Token count based on model**
        if 'gpt' in model:
            encoding = tiktoken.encoding_for_model(model)
            n_tokens = len(encoding.encode(prompt))

        elif 'gemini' in model or 'gemma' in model:
            try:
                n_tokens = len(prompt) // 4  # Adjust based on the response structure
                self.logger.debug(f"Rough estimate of token count for Gemini model '{model}': {n_tokens}")
            except Exception as e:
                self.logger.error(f"Error counting tokens for Gemini model '{model}': {e}")
                n_tokens = 0

        return n_tokens

    def parse_datasets_metadata(self, metadata: str, model='gemini-2.0-flash', use_portkey_for_gemini=True,
                                prompt_name='gpt_metadata_extract') -> dict:
        """
        Given the metadata, extract the dataset information using the LLM.

        :param metadata: str — the metadata to be parsed.

        :param model: str — the model to be used for parsing (default: 'gemini-2.0-flash').

        :return: dict — the extracted metadata. This is sometimes project metadata, or study metadata, or dataset metadata. Ontology enhancement is needed to distinguish between these.
        """
        #metadata = self.normalize_full_DOM(metadata)
        self.logger.info(f"Parsing metadata len: {len(metadata)}")
        dataset_info = self.extract_dataset_info(metadata, subdir='metadata_prompts',
                                                 use_portkey_for_gemini=use_portkey_for_gemini,
                                                 prompt_name=prompt_name)
        return dataset_info

    def flatten_metadata_dict(self, metadata: dict, parent_key: str = '', sep: str = '.') -> dict:
        """
        Recursively flattens a nested dictionary, concatenating keys with `sep`.
        Lists of dicts are expanded with their index.
        """
        items = []
        for k, v in metadata.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(self.flatten_metadata_dict(v, new_key, sep=sep).items())
            elif isinstance(v, list):
                for i, item in enumerate(v):
                    if isinstance(item, dict):
                        items.extend(self.flatten_metadata_dict(item, f"{new_key}[{i}]", sep=sep).items())
                    else:
                        items.append((f"{new_key}[{i}]", item))
            else:
                items.append((new_key, v))
        return dict(items)

    def extract_dataset_info(self, metadata, subdir='', model=None, use_portkey_for_gemini=True,
                             prompt_name='gpt_metadata_extract'):
        """
        Given the metadata, extract the dataset information using the LLM.

        :param model: str — the model to be used for parsing (default: self.llm_name).

        :param metadata: str — the metadata to be parsed.

        :param subdir: str — the subdirectory for the prompt template (default: '').

        :return: dict — the extracted metadata. This is sometimes project metadata, or study metadata, or dataset
         metadata
        """
        self.logger.info(f"Extracting dataset information from metadata. Prompt from subdir: {subdir}")

        llm = LLMClient(
            model=model if model else self.llm_name,
            logger=self.logger,
            save_prompts=self.save_dynamic_prompts,
            use_portkey_for_gemini=use_portkey_for_gemini
        )
        response = llm.api_call(metadata, subdir=subdir)

        # Post-process response into structured dict
        dataset_info = self.safe_parse_json(response)
        self.logger.info(f"Extracted dataset info: {dataset_info}")
        return dataset_info

    def semantic_retrieve_from_corpus(self, corpus, model_name='sentence-transformers/all-MiniLM-L6-v2',
                                      topk_docs_to_retrieve=5):
        """
        Given a corpus of text, retrieve the most relevant documents using semantic search.

        :param corpus: list of str — the corpus of text to search.

        :param model_name: str — the name of the embedding model to use (default: 'sentence-transformers/all-MiniLM-L6-v2').

        :param topk_docs_to_retrieve: int — the number of top documents to retrieve (default: 5).

        :return: list of dict — the most relevant documents from the corpus.
        """

        query = """Explicitly identify all the datasets by their database accession codes, repository names, and links
         to deposited datasets mentioned in this paper."""

        retriever = EmbeddingsRetriever(
            corpus=corpus,
            model_name=model_name,  # or any other model you prefer
            device="cpu",
            logger=self.logger
        )
        # Other queries can be used here as well, e.g.:
        # "Available data, accession code, data repository, deposited data"
        # "Explicitly identify all database accession codes, repository names, and links to deposited datasets or ...
        # ...supplementary data mentioned in this paper."
        # "Deposited data will be available in the repository XYZ, with accession code ABC123."
        # """Data availability statement, dataset reference, digital repository name, dataset identifier,
        #         dataset accession code, dataset doi, dataset page"""

        result = retriever.search(
            query=query,
            k=topk_docs_to_retrieve
        )

        return result


class LLMClient:
    def __init__(self, model: str, logger=None, save_prompts: bool = False, use_portkey_for_gemini=True):
        self.model = model
        self.logger = logger or logging.getLogger(__name__)
        self.logger.info(f"Initializing LLMClient with model: {self.model}")
        self.use_portkey_for_gemini = use_portkey_for_gemini
        self._initialize_client(model)
        self.save_prompts = save_prompts
        self.prompt_manager = PromptManager("data_gatherer/prompts/prompt_templates/metadata_prompts",
                                            self.logger)

    def _initialize_client(self, model):
        if model.startswith('gpt'):
            self.client = OpenAI(api_key=GPT_API_KEY)
        elif model.startswith('gemini') and not self.use_portkey_for_gemini:
            genai.configure(api_key=GEMINI_KEY)
            self.client = genai.GenerativeModel(model)
        elif model.startswith('gemini') and self.use_portkey_for_gemini:
            self.portkey = Portkey(
                api_key=PORTKEY_API_KEY,
                virtual_key=PORTKEY_ROUTE,
                base_url=PORTKEY_GATEWAY_URL,
                config=PORTKEY_CONFIG,
                metadata={"_user": DATA_GATHERER_USER_NAME}
            )
            self.client = self.portkey

        elif model.startswith('gemma'):
            self.client = Client(host="http://localhost:11434")

        else:
            self.client = None
        self.logger.info(f"Client initialized: {self.client}")

    def api_call(self, content, subdir='', **kwargs):
        self.logger.info(f"Calling {self.model} with prompt length {len(content)}, subdir: {subdir}")
        if self.model.startswith('gpt'):
            return self._call_openai(content, subdir=subdir)
        elif self.model.startswith('gemini'):
            if self.use_portkey_for_gemini:
                return self._call_portkey_gemini(content, subdir=subdir)
            else:
                return self._call_gemini(content, subdir=subdir)
        else:
            raise ValueError(f"Unsupported model: {self.model}")

    def _call_openai(self, content, temperature=0.0, subdir='', **kwargs):
        self.logger.info(f"Calling OpenAI with content length {len(content)}, subdir: {subdir}")
        messages = self.prompt_manager.render_prompt(
            self.prompt_manager.load_prompt("gpt_metadata_extract", subdir=subdir),
            entire_doc=True,
            content=content,
        )
        # save prompt_eval
        if self.save_prompts:
            self.prompt_manager.save_prompt(prompt_id='abc', prompt_content=messages)

        response = self.client.responses.create(
            model=self.model,
            input=messages,
            temperature=temperature,
            text={
                "format": kwargs.get('response_format', {"type": "json_object"})
            }
        )
        return response.output

    def _call_gemini(self, content, temperature=0.0, subdir=''):
        self.logger.info(f"Calling Gemini with content length {len(content)}, subdir: {subdir}")
        messages = self.prompt_manager.render_prompt(
            self.prompt_manager.load_prompt("gemini_metadata_extract", subdir=subdir),
            entire_doc=True,
            content=content,
        )

        # save prompt_eval
        if self.save_prompts:
            self.prompt_manager.save_prompt(prompt_id='abc', prompt_content=messages)

        response = self.client.generate_content(
            messages,
            generation_config=genai.GenerationConfig(
                response_mime_type="application/json",
                temperature=temperature,
            )
        )
        return response.text

    def _call_portkey_gemini(self, content, temperature=0.0, subdir=''):
        self.logger.info(f"Calling Gemini via Portkey with content length {len(content)}, subdir: {subdir}")
        # Render the prompt (should be a single message with 'parts')
        messages = self.prompt_manager.render_prompt(
            self.prompt_manager.load_prompt("portkey_gemini_metadata_extract", subdir=subdir),
            entire_doc=True,
            content=content,
        )
        if self.save_prompts:
            self.prompt_manager.save_prompt(prompt_id='abc', prompt_content=messages)

        portkey_payload = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
        }

        self.logger.debug(f"Portkey payload: {portkey_payload}")

        try:
            response = self.portkey.chat.completions.create(
                api_key=PORTKEY_API_KEY,
                route=PORTKEY_ROUTE,
                headers={"Content-Type": "application/json"},
                **portkey_payload
            )

            return response

        except Exception as e:
            raise RuntimeError(f"Portkey API call failed: {e}")
