import requests
from agents.weavr_agent.utils.license_checker import classify_license

def fetch_repo_metadata(source, url):
    """
    Placeholder metadata parser for GitHub, Hugging Face, DockerHub.
    In future, replace with proper API lookups or HTML scraping.
    """
    metadata = {
        "source": source,
        "url": url,
        "license": "MIT",
        "type": "tool",
        "name": url.split("/")[-1]
    }
    metadata["license_class"] = classify_license(metadata["license"])
    return metadata

def parse_sources(pipeline_targets):
    """
    Simulates open-source discovery using dummy URLs per source.
    Filters by license and type.
    """
    results = []

    dummy_sources = {
        "github": [
            "https://github.com/org/tool-a",
            "https://github.com/org/stack-gluer"
        ],
        "huggingface": [
            "https://huggingface.co/org/model-b"
        ],
        "dockerhub": [
            "https://hub.docker.com/r/org/agent-c"
        ]
    }

    for source in pipeline_targets:
        urls = dummy_sources.get(source, [])
        for url in urls:
            repo = fetch_repo_metadata(source, url)
            if repo["license_class"] == "safe":
                results.append(repo)

    return results
