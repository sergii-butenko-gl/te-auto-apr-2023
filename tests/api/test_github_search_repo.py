def test_search_repo_positive(fixture_git_hub_api_client):
    """
    This test seach for existing repo on GitHub
    """
    # Prepare the existing repo name
    repo_name = 'python'
    
    # Search for the repo from step #1
    repos_list = fixture_git_hub_api_client.search_repo(repo_name)
    
    # Validate the search returns results
    assert len(repos_list) != 0

def test_search_repo_negative(fixture_git_hub_api_client):
    """
    This test seach for existing repo on GitHub
    """
    # Prepare the existing repo name
    repo_name = 'alnsdihfbabsdiufhiuahsduyfbiuahsdiufhiuahsdfiuh'
    
    # Search for the repo from step #1
    repos_list = fixture_git_hub_api_client.search_repo(repo_name)
    
    # Validate the search returns results
    assert len(repos_list) == 0
