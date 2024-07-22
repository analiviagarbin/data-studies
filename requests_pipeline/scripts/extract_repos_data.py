from data_repos_class import RepositoryData

access_token = 'token'

amazon_rep = RepositoryData('Amazon', 'amzn', access_token)
amazon_rep.create_dt()

netflix_rep = RepositoryData('Netflix', 'netflix', access_token)
netflix_rep.create_dt()