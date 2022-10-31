
class AppBusiness:
    @staticmethod
    def get_zuri_profile():
        response = {
            'slackUsername': 'trustedcoder',
            'backend': True,
            'age': 30,
            'bio': 'Very simple person and loves coding. Video games makes me relax.'
        }
        return response, 200
