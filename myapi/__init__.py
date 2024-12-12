import falcon
import os

database_settings = {
    'host': os.getenv('MARIADB_HOST', 'localhost'),
    'port': int(os.getenv('MARIADB_PORT', '3306')),
    'database': os.getenv('MARIADB_DATABASE'),
    'user': os.getenv('MARIADB_USER'),
    'password': os.getenv('MARIADB_PASSWORD'),
}


class InfoResource:
    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        resp.media = {
            'database_settings': database_settings,
            'version': '1.1.0'
        }


app = falcon.App()
app.add_route('/info', InfoResource())
