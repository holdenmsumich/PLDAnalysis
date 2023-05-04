import os

DB_DETAILS = {
    'dev' : {
        'SOURCE_DB': {
            'DB_TYPE': 'mysql',
            'DB_HOST': '172.17.0.1',
            'DB_NAME': os.environ.get('DB_NAME'),
            'DB_USER': os.environ.get('DB_USER'),
            'DB_PASS': os.environ.get('DB_PASS')
        },
        'TARGET_DB': {
            'DB_TYPE': 'mysql',
            'DB_HOST': '172.17.0.1',
            'DB_NAME': os.environ.get('DB_NAME'),
            'DB_USER': os.environ.get('DB_USER'),
            'DB_PASS': os.environ.get('DB_PASS')
        }
    }
}