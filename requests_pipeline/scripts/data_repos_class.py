import requests
import pandas as pd

class RepositoryData:

    def __init__(self, company, owner, access_token):
        self.owner = owner
        self.company = company
        self.api_base_url = 'https://api.github.com'
        self.access_token = access_token
        self.headers = {'Authorization': 'Bearer ' + self.access_token,
                        'X-GitHub-Api-Version': '2022-11-28'}
        
    def repos_list(self):
        repos_list = []
        page = 1

        while True:
            try:
                url_page = f'{self.api_base_url}/users/{self.owner}/repos?page={page}'
                response = requests.get(url_page, headers=self.headers)
                
                if len(response.json()) == 0:
                    break
                
                repos_list.append(response.json())
                page += 1
            except:
                repos_list.append(None)

        return repos_list
    
    def repos_names(self, repos_list):
        repos_names = []

        for page in repos_list:
            for repo in page:
                try:
                    repos_names.append(repo['name'])
                except:
                    pass
        
        return repos_names

    def repos_lang(self, repos_list):
        repos_lang = []

        for page in repos_list:
            for repo in page:
                try:
                    repos_lang.append(repo['language'])
                except:
                    pass

        return repos_lang
    
    def create_dt(self):
        data_amz = pd.DataFrame()

        repos = self.repos_list()
        data_amz['repository_name'] = self.repos_names(repos)
        data_amz['language'] = self.repos_lang(repos)

        data_amz.to_csv(f'../data_processed/{self.company}.csv')