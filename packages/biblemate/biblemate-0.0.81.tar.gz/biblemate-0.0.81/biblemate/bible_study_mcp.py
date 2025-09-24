import logging, json, os
from fastmcp import FastMCP
from fastmcp.prompts.prompt import PromptMessage, TextContent
from agentmake import agentmake
from biblemate import BIBLEMATEDATA, AGENTMAKE_CONFIG, config
from biblemate.uba.bible import search_bible
from biblemate.uba.api import run_uba_api
from typing import List, Dict, Any, Union

# configure backend
AGENTMAKE_CONFIG["backend"] = config.backend

# Configure logging before creating the FastMCP server
logging.basicConfig(format="[%(levelname)s]: %(message)s", level=logging.ERROR)

mcp = FastMCP(name="BibleMate AI")

def getResponse(messages:list) -> str:
    return messages[-1].get("content") if messages and "content" in messages[-1] else "Error!"

'''@mcp.resource("resource://audio")
def audio() -> str:
    """UBA Bible Audio"""
    resources = json.loads(run_uba_api(".resources"))
    return "\n".join([f"- `{r}`" for r in resources["bibleAudioModules"]])'''

@mcp.resource("resource://bibles")
def bibles() -> dict:
    """UBA Bibles; usage examples: `//bible/John 3:16-18`, `//bible/KJV/John 3:16-18; Deut 6:4`"""
    resources = json.loads(run_uba_api(".resources"))
    return dict(zip(resources["bibleListAbb"], resources["bibleList"]))

@mcp.resource("bible://{module}/{reference}")
def bible(module:str, reference:str) -> dict:
    """UBA Bible; usage examples: `//bible/John 3:16-18`, `//bible/KJV/John 3:16-18; Deut 6:4`"""
    return run_uba_api(f"BIBLE:::{module}::{reference}")

@mcp.resource("resource://commentaries")
def commentaries() -> dict:
    """UBA Commentaries; usage examples: `//commentary/John 3:16`, `//commentary/CBSC/John 3:16`"""
    resources = json.loads(run_uba_api(".resources"))
    return dict(zip(resources["commentaryListAbb"], resources["commentaryList"]))

@mcp.resource("commentary://{module}/{reference}")
def commentary(module:str, reference:str) -> dict:
    """UBA Commentary; usage examples: `//commentary/John 3:16`, `//commentary/CBSC/John 3:16`"""
    return run_uba_api(f"COMMENTARY:::{module}::{reference}")

@mcp.resource("resource://data")
def data() -> str:
    """UBA Data; UBA command example: `DATA:::Bible Chronology`"""
    resources = json.loads(run_uba_api(".resources"))
    return "\n".join([f"- `{r}`" for r in resources["dataList"]])

@mcp.resource("resource://dictionaries")
def dictionaries() -> dict:
    """UBA Dictionaries; usage examples: `//dictionary/Jesus`, `//dictionary/Israel`"""
    resources = json.loads(run_uba_api(".resources"))
    return dict(zip(resources["dictionaryListAbb"], resources["dictionaryList"]))

dictionary_db = os.path.join(BIBLEMATEDATA, "dictionary.db")
if os.path.isfile(dictionary_db):
    @mcp.resource("dictionary://{query}")
    def dictionary(query:str) -> Union[str, list]:
        """UBA Dictionary; usage examples: `//dictionary/Jesus`, `//dictionary/Israel`"""
        from biblemate.uba.search import UBASearches
        dictionary_db = os.path.join(BIBLEMATEDATA, "dictionary.db")
        return UBASearches.search_data(
            db_file=dictionary_db,
            sql_table="Dictionary",
            query=query,
            top_k=config.max_semantic_matches,
        )

'''@mcp.resource("resource://docs")
def docs() -> str:
    """UBA Documents"""
    resources = json.loads(run_uba_api(".resources"))
    return "\n".join([f"- `{r}`" for r in resources["docxList"]])'''

@mcp.resource("resource://encyclopedias")
def encyclopedias() -> dict:
    """UBA Encyclopedias; usage examples: `//encyclopedia/Jesus`, `//encyclopedia/ISB/Jesus`"""
    resources = json.loads(run_uba_api(".resources"))
    return dict(zip(resources["encyclopediaListAbb"], resources["encyclopediaList"]))

encyclopedia_db = os.path.join(BIBLEMATEDATA, "encyclopedia.db")
if os.path.exists(encyclopedia_db):
    @mcp.resource("encyclopedia://{module}/{query}")
    def encyclopedia(module: str, query:str) -> Union[str, list]:
        """UBA Encyclopedia; usage examples: `//encyclopedia/Jesus`, `//encyclopedia/ISB/Jesus`"""
        from biblemate.uba.search import UBASearches
        encyclopedia_db = os.path.join(BIBLEMATEDATA, "encyclopedia.db")
        return UBASearches.search_data(
            db_file=encyclopedia_db,
            sql_table=module,
            query=query,
            top_k=config.max_semantic_matches,
        )

'''@mcp.resource("resource://epubs")
def epubs() -> str:
    """UBA EPUBs"""
    resources = json.loads(run_uba_api(".resources"))
    return "\n".join([f"- `{r}`" for r in resources["epubList"]])'''

@mcp.resource("resource://lexicons")
def lexicons() -> str:
    """UBA Lexicons; UBA command example: `LEXICON:::G25` or `LEXICON:::H3478`"""
    resources = json.loads(run_uba_api(".resources"))
    return "\n".join([f"- `{r}`" for r in resources["lexiconList"]])

'''@mcp.resource("resource://references")
def references() -> str:
    """UBA Reference Books"""
    resources = json.loads(run_uba_api(".resources"))
    return "\n".join([f"- `{r}`" for r in resources["referenceBookList"]])'''

'''@mcp.resource("resource://pdfs")
def pdfs() -> str:
    """UBA PDFs"""
    resources = json.loads(run_uba_api(".resources"))
    return "\n".join([f"- `{r}`" for r in resources["pdfList"]])'''

'''@mcp.resource("resource://searchtools")
def searchtools() -> str:
    """UBA Search Tools"""
    resources = json.loads(run_uba_api(".resources"))
    return "\n".join([f"- `{r}`" for r in resources["searchToolList"]])'''

@mcp.resource("resource://strongs")
def strongs() -> str:
    """UBA Strong's Bibles; UBA command example: `BIBLE:::KJVx:::John 3:16`"""
    resources = json.loads(run_uba_api(".resources"))
    return "\n".join([f"- `{r}`" for r in resources["strongBibleListAbb"]])

'''@mcp.resource("resource://thirddicts")
def thirddicts() -> str:
    """UBA Third-Party Dictionaries; UBA command examples: `SEARCHTHIRDDICTIONARY:::faith`, `SEARCHTHIRDDICTIONARY:::webster:::faith`"""
    resources = json.loads(run_uba_api(".resources"))
    return "\n".join([f"- `{r}`" for r in resources["thirdPartyDictionaryList"]])'''

@mcp.resource("resource://topics")
def topics() -> dict:
    """UBA Topical Collections; usage examples: `//topic/faith`, `//topic/hope`, `//topic/love`"""
    resources = json.loads(run_uba_api(".resources"))
    return dict(zip(resources["topicListAbb"], resources["topicList"]))

topic_db = os.path.join(BIBLEMATEDATA, "exlb.db")
if os.path.exists(topic_db):
    @mcp.resource("topic://{query}")
    def topic(query:str) -> Union[str, list]:
        """UBA Topical Studies; usage examples: `//topic/faith`, `//topic/hope`, `//topic/love`"""
        from biblemate.uba.search import UBASearches
        topic_db = os.path.join(BIBLEMATEDATA, "exlb.db")
        return UBASearches.search_data(
            db_file=topic_db,
            sql_table="exlbt",
            query=query,
            top_k=config.max_semantic_matches,
        )
    @mcp.resource("character://{query}")
    def character(query:str) -> Union[str, list]:
        """UBA Character Studies; usage examples: `//character/Jesus`, `//character/Samuel`, `//topic/John`"""
        from biblemate.uba.search import UBASearches
        topic_db = os.path.join(BIBLEMATEDATA, "exlb.db")
        return UBASearches.search_data(
            db_file=topic_db,
            sql_table="exlbp",
            query=query,
            top_k=config.max_semantic_matches,
        )
    @mcp.resource("location://{query}")
    def location(query:str) -> Union[str, list]:
        """UBA Location Studies; usage examples: `//location/Jerusalem`, `//location/Bethel`, `//location/Bethlehem`"""
        from biblemate.uba.search import UBASearches
        topic_db = os.path.join(BIBLEMATEDATA, "exlb.db")
        return UBASearches.search_data(
            db_file=topic_db,
            sql_table="exlbl",
            query=query,
            top_k=config.max_semantic_matches,
        )

@mcp.tool
def search_the_whole_bible(request:str) -> str:
    """search the whole bible; search string must be given"""
    global search_bible
    return search_bible(request)

@mcp.tool
def search_genesis_only(request:str) -> str:
    """search the book of Genesis only; search string must be given"""
    global search_bible
    return search_bible(request, book=1)

@mcp.tool
def search_exodus_only(request:str) -> str:
    """search the book of Exodus only; search string must be given"""
    global search_bible
    return search_bible(request, book=2)

@mcp.tool
def search_leviticus_only(request:str) -> str:
    """search the book of Leviticus only; search string must be given"""
    global search_bible
    return search_bible(request, book=3)

@mcp.tool
def search_numbers_only(request:str) -> str:
    """search the book of Numbers only; search string must be given"""
    global search_bible
    return search_bible(request, book=4)

@mcp.tool
def search_deuteronomy_only(request:str) -> str:
    """search the book of Deuteronomy only; search string must be given"""
    global search_bible
    return search_bible(request, book=5)

@mcp.tool
def search_joshua_only(request:str) -> str:
    """search the book of Joshua only; search string must be given"""
    global search_bible
    return search_bible(request, book=6)

@mcp.tool
def search_judges_only(request:str) -> str:
    """search the book of Judges only; search string must be given"""
    global search_bible
    return search_bible(request, book=7)

@mcp.tool
def search_ruth_only(request:str) -> str:
    """search the book of Ruth only; search string must be given"""
    global search_bible
    return search_bible(request, book=8)

@mcp.tool
def search_1_samuel_only(request:str) -> str:
    """search the book of 1 Samuel only; search string must be given"""
    global search_bible
    return search_bible(request, book=9)

@mcp.tool
def search_2_samuel_only(request:str) -> str:
    """search the book of 2 Samuel only; search string must be given"""
    global search_bible
    return search_bible(request, book=10)

@mcp.tool
def search_1_kings_only(request:str) -> str:
    """search the book of 1 Kings only; search string must be given"""
    global search_bible
    return search_bible(request, book=11)

@mcp.tool
def search_2_kings_only(request:str) -> str:
    """search the book of 2 Kings only; search string must be given"""
    global search_bible
    return search_bible(request, book=12)

@mcp.tool
def search_1_chronicles_only(request:str) -> str:
    """search the book of 1 Chronicles only; search string must be given"""
    global search_bible
    return search_bible(request, book=13)

@mcp.tool
def search_2_chronicles_only(request:str) -> str:
    """search the book of 2 Chronicles only; search string must be given"""
    global search_bible
    return search_bible(request, book=14)

@mcp.tool
def search_ezra_only(request:str) -> str:
    """search the book of Ezra only; search string must be given"""
    global search_bible
    return search_bible(request, book=15)

@mcp.tool
def search_nehemiah_only(request:str) -> str:
    """search the book of Nehemiah only; search string must be given"""
    global search_bible
    return search_bible(request, book=16)

@mcp.tool
def search_esther_only(request:str) -> str:
    """search the book of Esther only; search string must be given"""
    global search_bible
    return search_bible(request, book=17)

@mcp.tool
def search_job_only(request:str) -> str:
    """search the book of Job only; search string must be given"""
    global search_bible
    return search_bible(request, book=18)

@mcp.tool
def search_psalms_only(request:str) -> str:
    """search the book of Psalms only; search string must be given"""
    global search_bible
    return search_bible(request, book=19)

@mcp.tool
def search_proverbs_only(request:str) -> str:
    """search the book of Proverbs only; search string must be given"""
    global search_bible
    return search_bible(request, book=20)

@mcp.tool
def search_ecclesiastes_only(request:str) -> str:
    """search the book of Ecclesiastes only; search string must be given"""
    global search_bible
    return search_bible(request, book=21)

@mcp.tool
def search_song_of_songs_only(request:str) -> str:
    """search the book of Song of Songs only; search string must be given"""
    global search_bible
    return search_bible(request, book=22)

@mcp.tool
def search_isaiah_only(request:str) -> str:
    """search the book of Isaiah only; search string must be given"""
    global search_bible
    return search_bible(request, book=23)

@mcp.tool
def search_jeremiah_only(request:str) -> str:
    """search the book of Jeremiah only; search string must be given"""
    global search_bible
    return search_bible(request, book=24)

@mcp.tool
def search_lamentations_only(request:str) -> str:
    """search the book of Lamentations only; search string must be given"""
    global search_bible
    return search_bible(request, book=25)

@mcp.tool
def search_ezekiel_only(request:str) -> str:
    """search the book of Ezekiel only; search string must be given"""
    global search_bible
    return search_bible(request, book=26)

@mcp.tool
def search_daniel_only(request:str) -> str:
    """search the book of Daniel only; search string must be given"""
    global search_bible
    return search_bible(request, book=27)

@mcp.tool
def search_hosea_only(request:str) -> str:
    """search the book of Hosea only; search string must be given"""
    global search_bible
    return search_bible(request, book=28)

@mcp.tool
def search_joel_only(request:str) -> str:
    """search the book of Joel only; search string must be given"""
    global search_bible
    return search_bible(request, book=29)

@mcp.tool
def search_amos_only(request:str) -> str:
    """search the book of Amos only; search string must be given"""
    global search_bible
    return search_bible(request, book=30)

@mcp.tool
def search_obadiah_only(request:str) -> str:
    """search the book of Obadiah only; search string must be given"""
    global search_bible
    return search_bible(request, book=31)

@mcp.tool
def search_jonah_only(request:str) -> str:
    """search the book of Jonah only; search string must be given"""
    global search_bible
    return search_bible(request, book=32)

@mcp.tool
def search_micah_only(request:str) -> str:
    """search the book of Micah only; search string must be given"""
    global search_bible
    return search_bible(request, book=33)

@mcp.tool
def search_nahum_only(request:str) -> str:
    """search the book of Nahum only; search string must be given"""
    global search_bible
    return search_bible(request, book=34)

@mcp.tool
def search_habakkuk_only(request:str) -> str:
    """search the book of Habakkuk only; search string must be given"""
    global search_bible
    return search_bible(request, book=35)

@mcp.tool
def search_zephaniah_only(request:str) -> str:
    """search the book of Zephaniah only; search string must be given"""
    global search_bible
    return search_bible(request, book=36)

@mcp.tool
def search_haggai_only(request:str) -> str:
    """search the book of Haggai only; search string must be given"""
    global search_bible
    return search_bible(request, book=37)

@mcp.tool
def search_zechariah_only(request:str) -> str:
    """search the book of Zechariah only; search string must be given"""
    global search_bible
    return search_bible(request, book=38)

@mcp.tool
def search_malachi_only(request:str) -> str:
    """search the book of Malachi only; search string must be given"""
    global search_bible
    return search_bible(request, book=39)

@mcp.tool
def search_matthew_only(request:str) -> str:
    """search the book of Matthew only; search string must be given"""
    global search_bible
    return search_bible(request, book=40)

@mcp.tool
def search_mark_only(request:str) -> str:
    """search the book of Mark only; search string must be given"""
    global search_bible
    return search_bible(request, book=41)

@mcp.tool
def search_luke_only(request:str) -> str:
    """search the book of Luke only; search string must be given"""
    global search_bible
    return search_bible(request, book=42)

@mcp.tool
def search_john_only(request:str) -> str:
    """search the book of John only; search string must be given"""
    global search_bible
    return search_bible(request, book=43)

@mcp.tool
def search_acts_only(request:str) -> str:
    """search the book of Acts only; search string must be given"""
    global search_bible
    return search_bible(request, book=44)

@mcp.tool
def search_romans_only(request:str) -> str:
    """search the book of Romans only; search string must be given"""
    global search_bible
    return search_bible(request, book=45)

@mcp.tool
def search_1_corinthians_only(request:str) -> str:
    """search the book of 1 Corinthians only; search string must be given"""
    global search_bible
    return search_bible(request, book=46)

@mcp.tool
def search_2_corinthians_only(request:str) -> str:
    """search the book of 2 Corinthians only; search string must be given"""
    global search_bible
    return search_bible(request, book=47)

@mcp.tool
def search_galatians_only(request:str) -> str:
    """search the book of Galatians only; search string must be given"""
    global search_bible
    return search_bible(request, book=48)

@mcp.tool
def search_ephesians_only(request:str) -> str:
    """search the book of Ephesians only; search string must be given"""
    global search_bible
    return search_bible(request, book=49)

@mcp.tool
def search_philippians_only(request:str) -> str:
    """search the book of Philippians only; search string must be given"""
    global search_bible
    return search_bible(request, book=50)

@mcp.tool
def search_colossians_only(request:str) -> str:
    """search the book of Colossians only; search string must be given"""
    global search_bible
    return search_bible(request, book=51)

@mcp.tool
def search_1_thessalonians_only(request:str) -> str:
    """search the book of 1 Thessalonians only; search string must be given"""
    global search_bible
    return search_bible(request, book=52)

@mcp.tool
def search_2_thessalonians_only(request:str) -> str:
    """search the book of 2 Thessalonians only; search string must be given"""
    global search_bible
    return search_bible(request, book=53)

@mcp.tool
def search_1_timothy_only(request:str) -> str:
    """search the book of 1 Timothy only; search string must be given"""
    global search_bible
    return search_bible(request, book=54)

@mcp.tool
def search_2_timothy_only(request:str) -> str:
    """search the book of 2 Timothy only; search string must be given"""
    global search_bible
    return search_bible(request, book=55)

@mcp.tool
def search_titus_only(request:str) -> str:
    """search the book of Titus only; search string must be given"""
    global search_bible
    return search_bible(request, book=56)

@mcp.tool
def search_philemon_only(request:str) -> str:
    """search the book of Philemon only; search string must be given"""
    global search_bible
    return search_bible(request, book=57)

@mcp.tool
def search_hebrews_only(request:str) -> str:
    """search the book of Hebrews only; search string must be given"""
    global search_bible
    return search_bible(request, book=58)

@mcp.tool
def search_james_only(request:str) -> str:
    """search the book of James only; search string must be given"""
    global search_bible
    return search_bible(request, book=59)

@mcp.tool
def search_1_peter_only(request:str) -> str:
    """search the book of 1 Peter only; search string must be given"""
    global search_bible
    return search_bible(request, book=60)

@mcp.tool
def search_2_peter_only(request:str) -> str:
    """search the book of 2 Peter only; search string must be given"""
    global search_bible
    return search_bible(request, book=61)

@mcp.tool
def search_1_john_only(request:str) -> str:
    """search the book of 1 John only; search string must be given"""
    global search_bible
    return search_bible(request, book=62)

@mcp.tool
def search_2_john_only(request:str) -> str:
    """search the book of 2 John only; search string must be given"""
    global search_bible
    return search_bible(request, book=63)

@mcp.tool
def search_3_john_only(request:str) -> str:
    """search the book of 3 John only; search string must be given"""
    global search_bible
    return search_bible(request, book=64)

@mcp.tool
def search_jude_only(request:str) -> str:
    """search the book of Jude only; search string must be given"""
    global search_bible
    return search_bible(request, book=65)

@mcp.tool
def search_revelation_only(request:str) -> str:
    """search the book of Revelation only; search string must be given"""
    global search_bible
    return search_bible(request, book=66)

@mcp.tool
def compare_bible_translations(request:str) -> str:
    """compare Bible translations; bible verse reference(s) must be given"""
    global agentmake, getResponse
    messages = agentmake(request, **{'input_content_plugin': 'uba/every_single_ref', 'tool': 'uba/compare'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def retrieve_bible_study_indexes(request:str) -> str:
    """retrieve smart indexes on studying a particular bible verse; bible verse reference must be given"""
    global agentmake, getResponse
    messages = agentmake(request, **{'input_content_plugin': 'uba/every_single_ref', 'tool': 'uba/index'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def retrieve_bible_cross_references(request:str) -> str:
    """retrieve cross-references of Bible verses; bible verse reference(s) must be given"""
    global agentmake, getResponse
    messages = agentmake(request, **{'input_content_plugin': 'uba/every_single_ref', 'tool': 'uba/xref'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def retrieve_pointed_hebrew_or_accented_greek_bible_verses(request:str) -> str:
    """retrieve Hebrew (with pointed vowels) or Greek (with accents) Bible verses; bible verse reference(s) must be given, e.g. John 3:16-17; single or multiple references accepted, e.g. Deut 6:4; Gen 1:26-27"""
    global agentmake, getResponse
    messages = agentmake(request, **{'tool': 'uba/ohgb'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def retrieve_hebrew_or_greek_bible_verses(request:str) -> str:
    """retrieve Hebrew (without pointed vowels) or Greek (without accents) Bible verses; bible verse reference(s) must be given, e.g. John 3:16-17; single or multiple references accepted, e.g. Deut 6:4; Gen 1:26-27"""
    global agentmake, getResponse
    messages = agentmake(request, **{'tool': 'uba/mob'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def retrieve_english_bible_verses(request:str) -> str:
    """retrieve English Bible verses; bible verse reference(s) must be given, e.g. John 3:16-17; single or multiple references accepted, e.g. Deut 6:4; Gen 1:26-27"""
    global agentmake, getResponse
    messages = agentmake(request, **{'tool': 'uba/net'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def retrieve_english_bible_chapter(request:str) -> str:
    """retrieve a whole English Bible chapter; bible chapter reference must be given, e.g. John 3"""
    global agentmake, getResponse
    messages = agentmake(request, **{'tool': 'uba/net_chapter'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def retrieve_chinese_bible_verses(request:str) -> str:
    """retrieve Chinese Bible verses; bible verse reference(s) must be given, e.g. John 3:16-17; single or multiple references accepted, e.g. Deut 6:4; Gen 1:26-27"""
    global agentmake, getResponse
    messages = agentmake(request, **{'tool': 'uba/cuv'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def retrieve_chinese_bible_chapter(request:str) -> str:
    """retrieve a whole Chinese Bible chapter; bible chapter reference must be given, e.g. John 3"""
    global agentmake, getResponse
    messages = agentmake(request, **{'tool': 'uba/cuv_chapter'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def read_bible_commentary(request:str) -> str:
    """read bible commentary; bible verse reference(s) must be given"""
    global agentmake, getResponse
    messages = agentmake(request, **{'tool': 'uba/ai_comment'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def refine_bible_translation(request:List[Dict[str, Any]]) -> str:
    """refine the translation of a Bible verse or passage"""
    global agentmake, getResponse
    messages = agentmake(request, **{'system': 'bible/translate'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def write_pastor_prayer(request:List[Dict[str, Any]]) -> str:
    """write a prayer, out of a church pastor heart, based on user input"""
    global agentmake, getResponse
    messages = agentmake(request, **{'system': 'bible/pray'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def ask_theologian(request:List[Dict[str, Any]]) -> str:
    """ask a theologian about the bible"""
    global agentmake, getResponse
    messages = agentmake(request, **{'system': 'bible/theologian'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def quote_bible_verses(request:List[Dict[str, Any]]) -> str:
    """quote multiple bible verses in response to user request"""
    global agentmake, getResponse
    messages = agentmake(request, **{'system': 'bible/quote'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def anyalyze_psalms(request:List[Dict[str, Any]]) -> str:
    """analyze the context and background of the Psalms in the bible; Psalm reference must be given, e.g. Psalm 23:1-3"""
    global agentmake, getResponse
    messages = agentmake(request, **{'system': 'bible/david'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def ask_pastor(request:List[Dict[str, Any]]) -> str:
    """ask a church pastor about the bible"""
    global agentmake, getResponse
    messages = agentmake(request, **{'system': 'bible/billy'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def ask_bible_scholar(request:List[Dict[str, Any]]) -> str:
    """ask a bible scholar about the bible"""
    global agentmake, getResponse
    messages = agentmake(request, **{'system': 'bible/scholar'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def explain_bible_meaning(request:List[Dict[str, Any]]) -> str:
    """Explain the meaning of the user-given content in reference to the Bible"""
    global agentmake, getResponse
    messages = agentmake(request, **{'instruction': 'bible/meaning', 'system': 'auto'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def write_new_testament_historical_context(request:List[Dict[str, Any]]) -> str:
    """write the Bible Historical Context of a New Testament passage in the bible; new testament bible book / chapter / passage / reference(s) must be given"""
    global agentmake, getResponse
    messages = agentmake(request, **{'instruction': 'bible/nt_context', 'system': 'auto'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def write_bible_questions(request:List[Dict[str, Any]]) -> str:
    """Write thought-provoking questions for bible study group discussion; bible book / chapter / passage / reference(s) must be given"""
    global agentmake, getResponse
    messages = agentmake(request, **{'instruction': 'bible/questions', 'system': 'auto'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def write_bible_devotion(request:List[Dict[str, Any]]) -> str:
    """Write a devotion on a bible passage; bible book / chapter / passage / reference(s) must be given"""
    global agentmake, getResponse
    messages = agentmake(request, **{'instruction': 'bible/devotion', 'system': 'auto'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def translate_hebrew_bible_verse(request:List[Dict[str, Any]]) -> str:
    """Translate a Hebrew bible verse; Hebrew bible text must be given"""
    global agentmake, getResponse
    messages = agentmake(request, **{'instruction': 'bible/translate_hebrew', 'system': 'auto'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def write_bible_location_study(request:List[Dict[str, Any]]) -> str:
    """write comprehensive information on a bible location; a bible location name must be given"""
    global agentmake, getResponse
    messages = agentmake(request, **{'instruction': 'bible/location', 'system': 'auto'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def translate_greek_bible_verse(request:List[Dict[str, Any]]) -> str:
    """Translate a Greek bible verse: Greek bible text must be given"""
    global agentmake, getResponse
    messages = agentmake(request, **{'instruction': 'bible/translate_greek', 'system': 'auto'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def identify_bible_keywords(request:List[Dict[str, Any]]) -> str:
    """Identify bible key words from the user-given content"""
    global agentmake, getResponse
    messages = agentmake(request, **{'instruction': 'bible/keywords', 'system': 'auto'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def study_old_testament_themes(request:List[Dict[str, Any]]) -> str:
    """Study Bible Themes in a Old Testament passage; old testatment bible book / chapter / passage / reference(s) must be given"""
    global agentmake, getResponse
    messages = agentmake(request, **{'instruction': 'bible/ot_themes', 'system': 'auto'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def study_new_testament_themes(request:List[Dict[str, Any]]) -> str:
    """Study Bible Themes in a New Testament passage; new testament bible book / chapter / passage / reference(s) must be given"""
    global agentmake, getResponse
    messages = agentmake(request, **{'instruction': 'bible/nt_themes', 'system': 'auto'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def write_old_testament_highlights(request:List[Dict[str, Any]]) -> str:
    """Write Highlights in a Old Testament passage in the bible; old testament bible book / chapter / passage / reference(s) must be given"""
    global agentmake, getResponse
    messages = agentmake(request, **{'instruction': 'bible/ot_highligths', 'system': 'auto'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def write_bible_prayer(request:List[Dict[str, Any]]) -> str:
    """Write a prayer pertaining to the user content in reference to the Bible"""
    global agentmake, getResponse
    messages = agentmake(request, **{'instruction': 'bible/prayer', 'system': 'auto'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def write_short_bible_prayer(request:List[Dict[str, Any]]) -> str:
    """Write a short prayer, in one paragraph only, pertaining to the user content in reference to the Bible"""
    global agentmake, getResponse
    messages = agentmake(request, **{'instruction': 'bible/short_prayer', 'system': 'auto'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def write_bible_character_study(request:List[Dict[str, Any]]) -> str:
    """Write comprehensive information on a given bible character in the bible; a bible character name must be given"""
    global agentmake, getResponse
    messages = agentmake(request, **{'instruction': 'bible/character', 'system': 'auto'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def write_bible_thought_progression(request:List[Dict[str, Any]]) -> str:
    """write Bible Thought Progression of a bible book / chapter / passage; bible book / chapter / passage / reference(s) must be given"""
    global agentmake, getResponse
    messages = agentmake(request, **{'instruction': 'bible/flow', 'system': 'auto'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def quote_bible_promises(request:List[Dict[str, Any]]) -> str:
    """Quote relevant Bible promises in response to user request"""
    global agentmake, getResponse
    messages = agentmake(request, **{'instruction': 'bible/promises', 'system': 'auto'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def write_bible_chapter_summary(request:List[Dict[str, Any]]) -> str:
    """Write a detailed interpretation on a bible chapter; a bible chapter must be given"""
    global agentmake, getResponse
    messages = agentmake(request, **{'instruction': 'bible/chapter_summary', 'system': 'auto'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def write_bible_perspectives(request:List[Dict[str, Any]]) -> str:
    """Write biblical perspectives and principles in relation to the user content"""
    global agentmake, getResponse
    messages = agentmake(request, **{'instruction': 'bible/perspective', 'system': 'auto'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def interpret_old_testament_verse(request:List[Dict[str, Any]]) -> str:
    """Interpret the user-given bible verse from the Old Testament in the light of its context, together with insights of biblical Hebrew studies; an old testament bible verse / reference(s) must be given"""
    global agentmake, getResponse
    messages = agentmake(request, **{'instruction': 'bible/ot_meaning', 'system': 'auto'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def expound_bible_topic(request:List[Dict[str, Any]]) -> str:
    """Expound the user-given topic in reference to the Bible; a topic must be given"""
    global agentmake, getResponse
    messages = agentmake(request, **{'instruction': 'bible/topic', 'system': 'auto'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def write_bible_theology(request:List[Dict[str, Any]]) -> str:
    """write the theological messages conveyed in the user-given content, in reference to the Bible"""
    global agentmake, getResponse
    messages = agentmake(request, **{'instruction': 'bible/theology', 'system': 'auto'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def study_bible_themes(request:List[Dict[str, Any]]) -> str:
    """Study Bible Themes in relation to the user content"""
    global agentmake, getResponse
    messages = agentmake(request, **{'instruction': 'bible/themes', 'system': 'auto'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def write_bible_canonical_context(request:List[Dict[str, Any]]) -> str:
    """Write about canonical context of a bible book / chapter / passage; bible book / chapter / passage / reference(s) must be given"""
    global agentmake, getResponse
    messages = agentmake(request, **{'instruction': 'bible/canon', 'system': 'auto'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def write_bible_related_summary(request:List[Dict[str, Any]]) -> str:
    """Write a summary on the user-given content in reference to the Bible"""
    global agentmake, getResponse
    messages = agentmake(request, **{'instruction': 'bible/summary', 'system': 'auto'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def interpret_new_testament_verse(request:List[Dict[str, Any]]) -> str:
    """Interpret the user-given bible verse from the New Testament in the light of its context, together with insights of biblical Greek studies; a new testament bible verse / reference(s) must be given"""
    global agentmake, getResponse
    messages = agentmake(request, **{'instruction': 'bible/nt_meaning', 'system': 'auto'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def write_new_testament_highlights(request:List[Dict[str, Any]]) -> str:
    """Write Highlights in a New Testament passage in the bible; new testament bible book / chapter / passage / reference(s) must be given"""
    global agentmake, getResponse
    messages = agentmake(request, **{'instruction': 'bible/nt_highlights', 'system': 'auto'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def write_bible_applications(request:List[Dict[str, Any]]) -> str:
    """Provide detailed applications of a bible passages; bible book / chapter / passage / reference(s) must be given"""
    global agentmake, getResponse
    messages = agentmake(request, **{'instruction': 'bible/application', 'system': 'auto'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def write_bible_book_introduction(request:List[Dict[str, Any]]) -> str:
    """Write a detailed introduction on a book in the bible; bible book must be given"""
    global agentmake, getResponse
    messages = agentmake(request, **{'instruction': 'bible/introduce_book', 'system': 'auto'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def write_old_testament_historical_context(request:List[Dict[str, Any]]) -> str:
    """write the Bible Historical Context of a Old Testament passage in the bible; old testament bible book / chapter / passage / reference(s) must be given"""
    global agentmake, getResponse
    messages = agentmake(request, **{'instruction': 'bible/ot_context', 'system': 'auto'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def write_bible_outline(request:List[Dict[str, Any]]) -> str:
    """provide a detailed outline of a bible book / chapter / passage; bible book / chapter / passage / reference(s) must be given"""
    global agentmake, getResponse
    messages = agentmake(request, **{'instruction': 'bible/outline', 'system': 'auto'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def write_bible_insights(request:List[Dict[str, Any]]) -> str:
    """Write exegetical insights in detail on a bible passage; bible book / chapter / passage / reference(s) must be given"""
    global agentmake, getResponse
    messages = agentmake(request, **{'instruction': 'bible/insights', 'system': 'auto'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def write_bible_sermon(request:List[Dict[str, Any]]) -> str:
    """Write a bible sermon based on a bible passage; bible book / chapter / passage / reference(s) must be given"""
    global agentmake, getResponse
    messages = agentmake(request, **{'instruction': 'bible/sermon', 'system': 'auto'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.tool
def uba(request:str) -> str:
    """Execute an UBA command; a valid UBA command must be given; do not use this tool if you are not sure what you are doing"""
    global agentmake, getResponse
    messages = agentmake(request, **{'tool': 'uba/cmd'}, **AGENTMAKE_CONFIG)
    return getResponse(messages)

@mcp.prompt
def simple_bible_study(request:str) -> PromptMessage:
    """Perform a simple bible study task"""
    global PromptMessage, TextContent
    prompt_text = f"""You are a bible study agent. You check the user request, under the `User Request` section, and resolve it with the following steps in order:
1. Call tool 'retrieve_english_bible_verses' for Bible text, 
2. Call tool 'retrieve_bible_cross_references' for Bible cross-references, 
3. Call tool 'study_old_testament_themes' for studying old testament themes or 'study_new_testament_themes' for studying new testament themes, and 
4. Call tool 'write_bible_theology' to explain its theology.

# User Request

---
{request}
---
"""
    return PromptMessage(role="user", content=TextContent(type="text", text=prompt_text))

@mcp.prompt
def bible_devotion(request:str) -> PromptMessage:
    """Write bible devotion based on user content"""
    global PromptMessage, TextContent
    prompt_text = f"""
You are a bible devotional agent. You check the user content, under the `User Content` section, and write a devotional about it with the following steps in order:

1. Analyze the themes using @study_new_testament_themes for new testament passages or @study_old_testament_themes for old testament passages.
2. Identify and explain key biblical keywords from the passage using @identify_bible_keywords.
3. Write insights for the devotion using @write_bible_insights.
4. Relate the passage to daily life using @write_bible_applications.
5. Compose a touching devotion using @write_bible_devotion.
Ensure each step is clearly addressed and the final output is cohesive and inspiring.

# User Content

---
{request}
---
"""
    return PromptMessage(role="user", content=TextContent(type="text", text=prompt_text))

mcp.run(show_banner=False)