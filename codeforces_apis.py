import requests
from pprint import pprint

class Contest:

    # Takes an integer contest_id 
    # Returns a list of dicts of all users that participated in the contests and their rating changes
    @staticmethod
    def rating_changes(contest_id):

        params = {}
        url = "https://codeforces.com/api/contest.ratingChanges";

        params['contestId'] = contest_id

        response = requests.get(url,params)
        data = response.json()

        return data


    # Takes an integer contest_id and a list of handles of type string
    # Returns a list of dicts of 
    @staticmethod
    def standings(contest_id,handles):

        params = {}
        url = "https://codeforces.com/api/contest.standings";
        
        params['contestId'] = contest_id
        params['handles'] = ";".join(handles)

        response = requests.get(url,params)
        data = response.json()

        return data


class User:
    @staticmethod
    def user_info(handles:list[str]):
        params = {}
        url = "https://codeforces.com/api/user.info"

        params['handles'] = ";".join(handles)

        response = requests.get(url,params)
        data = response.json()
        pprint(data)
        return data

    @staticmethod
    def rating(handle:str):
        params = {}
        url = "https://codeforces.com/api/user.rating"

        params['handle'] = handle

        response = requests.get(url,params)
        data = response.json()

        return data



if __name__ == '__main__':
    User.rating("NapSaq")