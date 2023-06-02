try:
    from app import app
    import unittest
    from app import qa
    from flask import json


except Exception as ex1:
    print('Smth is missing {}'.format(ex1))


class FlaskTest(unittest.TestCase):

    def test_get(self):
        tester = app.test_client()
        response = tester.get('/')
        status_code = response.status_code

        assert response.status_code == 200
        assert "OK" == response.get_data(as_text=True)

    def test_post(self):
        for key in qa.keys():
            response = app.test_client().post(
                '/model/',
                data=json.dumps(dict(question=str(key))),
                content_type='application/json',
            )
            data = json.loads(response.get_data(as_text=True))
            print(str(key),data)

            assert response.status_code == 200
            assert data == qa[str(key)]

    def test_post_notin(self):
        response = app.test_client().post(
            '/model/',
            data=json.dumps(dict(question='smth different')),
            content_type='application/json',
        )
        data = json.loads(response.get_data(as_text=True))
        print('smth different',data)

        assert response.status_code == 200
        assert data == 'not implemented'


if __name__ == "__main__":
    unittest.main()
