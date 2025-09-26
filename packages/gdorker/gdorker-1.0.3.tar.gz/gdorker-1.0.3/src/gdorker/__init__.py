#!/usr/bin/env python
import argparse
import json
import os
import time
import signal
from typing import Dict, List, Optional, Any, NoReturn, Callable, Union
from types import TracebackType
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from colorama import init, Fore
import sys
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import re
import requests
from duckduckgo_search import DDGS

init(autoreset=True)

banner = """
⠀⠀⣠⣶⣶⣦⣤⡄⠀⠀⠀⠀⠀⠀⠀⢠⣤⣤⣤⣀⣀⡀⠀⠀⠀⠀⣠⣤⣤⣤⣄⠀⠀⠀⣤⣤⣤⣤⣤⣀⡀⠀⠀⣀⣀⣤⡀⢠⣤⣤⣤⠀⣀⣀⣀⣤⣤⣤⣤⡄⠀⢠⣤⣤⣤⣤⣄⣀⠀⠀
⠀⣼⡟⠁⠀⠉⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⠉⠙⠻⣷⡄⠀⠀⣼⡿⠁⠀⠀⢻⡆⠀⠀⠘⣿⠀⠀⠈⢹⣷⠀⠀⠈⢿⡏⠀⣨⡿⠋⠀⠀⠈⣿⡏⠉⢉⠙⣿⡇⠀⠀⢻⡏⠀⠀⠉⣻⡇⠀
⠀⣿⡇⠀⢠⣦⣼⣷⣦⠄⠀⠀⠀⠀⠀⠀⢸⣧⠀⠀⠀⠸⣷⠀⠀⣿⠇⠀⠀⠀⠀⣿⠀⠀⠀⣿⡶⠶⣾⡟⠁⠀⠀⠀⢸⣀⣴⣿⡀⠀⠀⠀⠀⢸⣷⣶⣿⡇⠈⠀⠀⠀⠸⣷⠶⢶⣾⠟⠀⠀
⠀⢺⣇⠀⠀⠀⢹⣿⠀⠸⠿⠿⠾⠿⠗⠀⢘⣿⠀⠀⠀⢠⡿⠀⠀⣿⡆⠀⠀⠀⢠⡟⠀⠀⠀⢹⡁⠀⢸⣧⠀⠀⠀⠀⢸⠟⠁⠙⢷⡀⠀⠀⠀⢸⡇⠀⠙⠃⢠⣤⠀⠀⠀⣏⠀⠀⢻⣆⠀⠀
⠀⠈⠻⣷⣶⣴⣿⡿⠀⠀⠀⠀⠀⠀⠀⣤⣼⣿⣤⣠⣴⠿⠁⠀⠀⠘⠿⣦⣤⣤⠟⠀⠀⠀⢠⣿⣧⣄⢀⣿⣷⣤⠀⣠⣽⣄⡀⢀⣠⣷⣤⠀⣠⣿⣷⣤⣴⣴⣾⣿⠀⠀⢴⣿⣦⡀⣸⣿⣦⡄
                               
                               By La1n
"""

# Google Custom Search API discovery identifiers
SERVICE_NAME = "customsearch"
SERVICE_VERSION = "v1"

# todo: errors NoMoreResultsException and ResourceExhaustedException
# todo: async requests
# todo: save data inside session class and pass it google search

class Formatter:
    def __init__(self, options: Dict[str, Any]) -> None:
        self.options: Dict[str, Any] = options
        self.is_extended: bool = self.options['code'] or (self.options['body'] and self.options['engine'] != 'duckduckgo')

    def _title(self, title: str) -> str:
        return f"{Fore.MAGENTA}[{title}]"

    def _url(self, url: str) -> str:
        return f"{Fore.GREEN}[{url}]"

    def _code(self, code: int) -> str:
        color = Fore.WHITE
        if code >= 200 and code < 300:
            color = Fore.GREEN
        elif code >= 300 and code < 400:
            color = Fore.YELLOW
        elif code >= 400 and code < 600:
            color = Fore.RED
        return f"{color}[{code}]"

    def _body(self, html: str) -> str:
        soup = BeautifulSoup(html, 'html.parser')
        body: str = soup.body.get_text() if soup.body else ""
        text: str = re.sub(r'[\s]+', " ", body).strip()[0:100]
        return f"{Fore.CYAN}[{text}]"

    def debug(self, info: str) -> str:
        return f"{Fore.LIGHTBLACK_EX}[DEBUG] {info}"

    def info(self, info: str) -> str:
        return f"{Fore.BLUE}[INFO] {info}"

    def error(self, error: str) -> str:
        return f"{Fore.RED}[ERROR] {error}"

    def _result(self, info: str) -> str:
        return f"{Fore.BLUE}[URL] {info}"

    def result(self, pieces: Dict[str, str]) -> str:
        output = [self._url(pieces["url"])]

        if self.options['code']:
            output.append(self._code(pieces["code"]))
        if self.options['title']:
            output.append(self._title(pieces['title']))
        if self.options['body']:
            output.append(self._body(pieces["body"]))
        return self._result(' '.join(output))


class Logger:
    def __init__(self, options: Dict[str, Any]) -> None:
        self.dest = options['dest']
        self.debug_enabled = options['debug']
        self.formatter = Formatter(options)
        if self.dest and isinstance(self.dest, str):
            self.dest = open(self.dest, 'a')

    def _write(self, line: str) -> None:
        print(line)

    def url(self, pieces: Dict[str, str]) -> None:
        line = self.formatter.result(pieces)
        self._write(line)
        if self.dest:
            print(line, file=self.dest)

    def info(self, info: str) -> None:
        line = self.formatter.info(info)
        self._write(line)

    def error(self, error: str) -> None:
        line = self.formatter.error(error)
        self._write(line)

    def debug(self, info: str) -> None:
        if not self.debug_enabled:
            return
        line = self.formatter.debug(info)
        self._write(line)

    def __exit__(self, exc_type, exc_value, traceback: Optional[TracebackType]) -> None:
        if self.dest:
            self.dest.close()


class Dorker:
    per_page = 10

    def __init__(self, logger: Logger, client: Callable[[str, int, int], Dict[str, Any]], error_handler) -> None:
        self.logger = logger
        self.offset: int = 0
        self.is_limit_reached = False
        self.client = client
        self.error_handler = error_handler

    @property
    def _page(self) -> int:
        return self.offset // self.per_page + 1

    def _search(self, query: str, start: int = 0) -> List[Dict[str, Any]]:
        try:
            self.logger.debug(f"Searching query='{query.strip()}' start={start} per_page={self.per_page}")
            res = self.client(query, start, self.per_page)
            self.logger.debug(f"Raw response keys: {list(res.keys()) if isinstance(res, dict) else type(res)}")
            items = res.get('items', [])
            if len(items) == 0:
                self.logger.info("No more links for current query")
                return []
            self.logger.debug(f"Fetched {len(items)} items")
            return items
        except Exception as e:
            self.logger.debug(f"Exception in _search: {e}")
            self.logger.debug(f"Exception details: type={type(e).__name__} repr={e!r}")
            return self.error_handler(e)

    async def _print_results_extended(self, results: List[Dict[str, Any]]) -> None:
        async def fetch(session, item):
            async with session.get(item['link']) as response:
                self.logger.debug(f"Fetch {item['link']} -> {response.status}")
                text = await response.text()
                return (item, response.status, text)
        async with aiohttp.ClientSession() as session:
            tasks = [fetch(session, item) for item in results]
            fetched = await asyncio.gather(*tasks)
            for item, status, body in fetched:
                pieces = {
                    "url": item['link'],
                    "title": item['title'],
                    "code": status,
                    "body": body
                }
                self.logger.url(pieces)

    def _print_results(self, results: List[Dict[str, Any]]) -> None:
        self.logger.debug(f"Printing {len(results)} results; extended={self.logger.formatter.is_extended}")
        if self.logger.formatter.is_extended:
            return asyncio.run(self._print_results_extended(results))
        for item in results:
            pieces = {
                "url": item['link'],
                "title": item['title']
            }
            self.logger.url(pieces)

    def query_results(self, query: str, offset: Optional[int]) -> None:
        if offset is None:
            offset = 0
        self.offset: int = offset
        self.query = query
        while not self.is_limit_reached:
            self.logger.info(f"Page {self._page}")
            self.logger.debug(f"Current offset={self.offset} limit_reached={self.is_limit_reached}")
            results = self._search(query, start=self.offset)
            self._print_results(results)
            if not results:
                break
            self.offset = self.offset + self.per_page
            self.logger.debug(f"Next offset will be {self.offset}")
            time.sleep(1)

class Session:
    def __init__(self, file: str) -> None:
        self.file = file

    def load(self) -> Dict[str, Any]:
        with open(self.file, "r") as f:
            j = json.loads(f.read())
            return j

    def clean(self) -> None:
        os.remove(self.file)

    def save(self, file_or_query: Union[str, List[str]], logger: Logger, gs: Dorker) -> None:
        session = {
            'file_or_query': file_or_query,
            'options': logger.formatter.options,
            'current_query': gs.query,
            'offset': gs.offset
        }
        j = json.dumps(session, indent=2)
        with open(self.file, 'w') as f:
            f.write(j)

def handle_exit_signal(session: Optional[Session], save_enabled: bool, file_or_query: str, logger: Logger, gs: Dorker) -> NoReturn:
    if save_enabled and session is not None:
        logger.info("Interrupted by user, saving session...")
        session.save(file_or_query, logger, gs)
    exit(0)

def load_queries(file_or_query: str) -> List[str]:
    try:
        with open(file_or_query, 'r') as f:
            queries = f.readlines()
            unique = list(set(queries))
            return unique
    except Exception as e:
        return [file_or_query]

class ConfigManager:
    def __init__(self, config_path='~/.config/gdorker/config.json'):
        self.api_key = None
        self.cse_id = None
        self.config_path = os.path.expanduser(config_path)
        self.default_content = {
            "google_api_key": "",
            "google_cse_id": ""
        }
        self._ensure_config_exists()
        
    def _ensure_config_exists(self):
        os.makedirs(os.path.dirname(self.config_path), exist_ok=True)
        if not os.path.isfile(self.config_path):
            # Try to copy packaged example config first
            try:
                example_path = os.path.join(os.path.dirname(__file__), 'config.example.json')
                with open(example_path, 'r') as src:
                    example_content = src.read()
                with open(self.config_path, 'w') as dst:
                    dst.write(example_content)
            except Exception:
                # Fallback to default content
                with open(self.config_path, 'w') as f:
                    json.dump(self.default_content, f, indent=4)
    
    def load_api_keys(self):
        with open(self.config_path, 'r') as f:
            return json.load(f)
    
    def set_api_keys(self, api_key, cse_id):
        self.api_key = api_key
        self.cse_id = cse_id

    def get_google_api_keys(self):
        api_keys = self.load_api_keys()
        api_key = api_keys.get('google_api_key', '') or self.api_key
        cse_id = api_keys.get('google_cse_id', '') or self.cse_id
        if api_key and cse_id and (not len(api_key) or not len(cse_id)):
            raise ValueError("API Key and CSE ID must be set in the configuration file.")
            
        return api_key, cse_id

class SearchClient:
    def __init__(self, search_engine='google', config: ConfigManager = None):
        self.search_engine = search_engine
        self.config = config
        
        if search_engine == 'google':
            self.api_key, self.cse_id = self.config.get_google_api_keys()
            self.client = self._create_google_client()
        elif search_engine == 'duckduckgo':
            self.client = self._create_duckduckgo_client()
        else:
            raise ValueError(f"Unsupported search engine: {search_engine}")

    def _create_google_client(self):
        def search(query: str, start: int, per_page: int) -> Dict[str, Any]:
            self.logger.debug(f"[google] query='{query.strip()}' start={start} per_page={per_page} cx_set={bool(self.cse_id)} key_set={bool(self.api_key)}")
            # Google CSE uses 1-based start index. We convert offset (0,10,20,...) to (1,11,21,...)
            start_index = (start or 0) + 1
            if start_index < 1:
                start_index = 1
            self.logger.debug(f"[google] discovery service={SERVICE_NAME} version={SERVICE_VERSION}")
            svc = build(SERVICE_NAME, SERVICE_VERSION, developerKey=self.api_key, static_discovery=False)
            req = svc.cse().list(q=query, cx=self.cse_id, start=start_index, num=per_page)
            try:
                res = req.execute()
            except HttpError as he:
                # Surface concise info; full content parsed in error_handler
                status_code = getattr(he, 'status_code', None)
                reason = getattr(he, 'reason', None)
                self.logger.error(f"Google HTTP error{f' {status_code}' if status_code else ''}: {reason or str(he)}")
                raise
            self.logger.debug(f"[google] response keys: {list(res.keys())}")
            return res
        return search
    
    def _create_duckduckgo_client(self):
        def search(query: str, start: int, per_page: int) -> Dict[str, Any]:
            try:
                self.logger.debug(f"[ddg] query='{query.strip()}' requested start={start} per_page={per_page}")
                results = []
                with DDGS() as ddgs:
                    for r in ddgs.text(query, max_results=1000):
                        results.append({
                            'title': r['title'],
                            'link': r['href'],
                            'body': r['body']
                        })
                if not results:
                    self.logger.info("No more links for current query")
                    return {'items': []}
                self.logger.debug(f"[ddg] total gathered={len(results)} returning slice 0:{per_page}")
                return {'items': results}
            except Exception as e:
                self.logger.debug(f"[ddg] exception: {e}")
                raise Exception(f"DuckDuckGo search error: {str(e)}")
            
        return search
    
    def search(self, query, start, per_page):
        return self.client(query, start, per_page)

    def error_handler(self, e: Exception):
        if self.search_engine == 'google':
            # Prefer specific handling for HttpError
            if isinstance(e, HttpError):
                raw_content = getattr(e, 'content', None)
                if isinstance(raw_content, bytes):
                    raw_content = raw_content.decode('utf-8', errors='ignore')
                if raw_content:
                    try:
                        error_content = json.loads(raw_content)
                        status = error_content.get('error', {}).get('status')
                        message = error_content.get('error', {}).get('message')
                        self.logger.error(f"Google API error: {status or 'UNKNOWN'} - {message or 'No message'}")
                        if status == 'RESOURCE_EXHAUSTED':
                            self.logger.info("Resource limit reached")
                            raise e
                        if status == 'INVALID_ARGUMENT':
                            self.logger.info("No more links for current query")
                    except json.JSONDecodeError:
                        self.logger.error(raw_content)
                else:
                    self.logger.error(f"Google API error (no content): {str(e)}")
                return []
            # Fallback generic error
            self.logger.error(f"Google API error (unexpected type {type(e).__name__}): {str(e)}")
            return []
        elif self.search_engine == 'duckduckgo':
            if '202' in str(e):
                self.logger.info("Resource limit reached")
                raise e
            else:
                self.logger.error(f"DuckDuckGo error: {str(e)}")
            return []
        else:
            raise Exception('not implemented yet')


def main(client: SearchClient, file_or_query: str, resume: bool, session_path: Optional[str], options: Dict[str, Any]) -> None:
    current_query = None
    offset = None
    session: Optional[Session] = None
    save_enabled = options.get('save_session', False)
    if resume and session_path:
        session = Session(session_path)
        data = session.load()
        file_or_query = data['file_or_query']
        options = data['options']
        offset = data['offset']
        current_query = data['current_query']
    elif save_enabled and session_path:
        session = Session(session_path)

    logger = Logger(options)
    client.logger = logger
    logger.info(f"Using {client.search_engine} as search engine")
    logger.debug(f"Options: title={options['title']} body={options['body']} code={options['code']} debug={options['debug']} dest_set={bool(options['dest'])}")
    dorker = Dorker(logger, client.search, client.error_handler)

    logger.debug(f"Loading queries from '{file_or_query}' resume={resume}")
    queries = load_queries(file_or_query)
    logger.debug(f"Loaded {len(queries)} queries")
    if current_query:
        index = next((i for i, q in enumerate(queries) if q == current_query), len(queries))
        queries = queries[index:]

    if save_enabled and session is not None:
        signal.signal(signal.SIGINT, lambda signum, frame: handle_exit_signal(
            session, save_enabled, file_or_query, logger, dorker))
        
    for i, query in enumerate(queries):
        logger.info(f"Query: {query}")
        logger.debug(f"Starting query index={i} content_length={len(query.strip())}")
        try:
            dorker.query_results(query, offset)
            if save_enabled and session is not None:
                session.save(file_or_query, logger, dorker)
            logger.debug("Session saved after successful query run")
        except Exception as e:
            if i:
                logger.error(f"Error during query execution: {e}")
            if save_enabled and session is not None:
                session.save(file_or_query, logger, dorker)
            logger.debug("Session saved after error")
            exit(1)
        if dorker.is_limit_reached:
            if save_enabled and session is not None:
                session.save(file_or_query, logger, dorker)
            logger.debug("Session saved due to limit reached")
            exit(1)
    if save_enabled and session is not None:
        session.clean()
    logger.debug("Session file removed; all queries completed")

def entrypoint():
    print(banner)
    parser = argparse.ArgumentParser(
        description="""
G-Dorker - Google Custom Search Engine Dorking Tool

A tool for performing Google dorks using Custom Search Engine API.
Allows saving results to file and extracting additional information from URLs.
""",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    ./gdorker.py -q "site:example.com" -k YOUR_API_KEY -x YOUR_CSE_ID
    ./gdorker.py -q "inurl:admin" -k YOUR_API_KEY -x YOUR_CSE_ID -t -c -b
    ./gdorker.py -q "filetype:pdf" -k YOUR_API_KEY -x YOUR_CSE_ID -f results.txt -b
    ./gdorker.py -q ./bb_dorks.txt -k YOUR_API_KEY -x YOUR_CSE_ID -f results.txt -b --engine duckduckgo
    ./gdorker.py -q ./bb_dorks.txt -k YOUR_API_KEY -x YOUR_CSE_ID -f results.txt --session ./gdorker_session_1744260850.json
Config file is located in ~/.config/gdorker/config.json
    You can set your API key and CSE ID there, so you don't need to pass them every time.
""")

    required = parser.add_argument_group('Required arguments')
    required.add_argument(
        "-q", "--query",
        help="Search query (Google dork string) or path to file with queries"
    )
    required.add_argument(
        "-k", "--api-key",
        help="Google Custom Search API key"
    )
    required.add_argument(
        "-x", "--cx",
        help="Google Custom Search Engine ID"
    )

    output = parser.add_argument_group('Output options')
    output.add_argument(
        "-f", "--file",
        help="Save results to file"
    )
    output.add_argument(
        "-t", "--title",
        action="store_true",
        help="Include page title"
    )
    output.add_argument(
        "-d", "--debug",
        action="store_true",
        help="Debug output"
    )
    output.add_argument(
        "-s", "--session",
        help="Resume from"
    )
    output.add_argument(
        "--save-session",
        action="store_true",
        help="Persist progress to a session file (creates one if omitted)"
    )

    content = parser.add_argument_group('Options that trigger additional request for each URL')
    content.add_argument(
        "-c", "--code",
        action="store_true",
        help="Include HTTP status codes"
    )
    content.add_argument(
        "-b", "--body",
        action="store_true",
        help="Include first 100 chars of page body (no extra request for duckduckgo)"
    )

    parser.add_argument(
        "-e", "--engine",
        default="google",
        choices=["google", "duckduckgo"],
        help="Search engine to use"
    )

    args = parser.parse_args()
    options = {
        'title': args.title,
        'body': args.body,
        'code': args.code,
        'dest': args.file,
        'debug': args.debug,
        'engine': args.engine,
        'save_session': args.save_session
    }

    #if args.debug:
    #    print(dir(Fore))

    if not args.query and not args.session:
        raise ValueError("No query specified")

    session_path = args.session
    resume = bool(session_path)
    if not session_path and options['save_session']:
        current_dir = os.getcwd()
        session_path = os.path.join(current_dir, f"gdorker_session_{int(time.time())}.json")

    config = ConfigManager()
    if args.api_key and args.cx:
        config.set_api_keys(args.api_key, args.cx)
    else:
        # surface what config we are about to use without leaking secrets
        try:
            api_key_masked, cse_id_masked = None, None
            keys = config.load_api_keys()
            api_key_val = keys.get('google_api_key', '')
            cse_id_val = keys.get('google_cse_id', '')
            api_key_masked = (api_key_val[:4] + "..." + api_key_val[-4:]) if api_key_val else None
            cse_id_masked = (cse_id_val[:4] + "..." + cse_id_val[-4:]) if cse_id_val else None
            # We do not log full secrets, only whether present and masked heads/tails
            # Debug only when enabled
            if options['debug']:
                print(Formatter(options).debug(f"Using config: key_set={bool(api_key_val)} key={api_key_masked} cx_set={bool(cse_id_val)} cx={cse_id_masked}"))
        except Exception:
            # ignore config logging issues
            pass

    search_client = SearchClient(args.engine, config)
    main(search_client, args.query, resume, session_path, options)

if __name__ == "__main__":
    entrypoint()
