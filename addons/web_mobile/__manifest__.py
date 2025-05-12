# -*- coding: utf-8 -*-

{
    'name': 'Mobile',
    'category': 'Website/Website WL20',
    'summary': 'Wl20 Mobile Core module',
    'version': '1.0',
    'description': """

        """,
    'depends': [
        'web_wl20_e',
    ],
    'data': [
        'views/views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'web_mobile/static/src/**/*',
        ],
        # 'web.assets_unit_tests': [
        #     "web_mobile/static/tests/**/*.test.js",
        # ],
        # 'web.tests_assets': [
        #     'web_mobile/static/tests/helpers/**/*',
        # ],
        # 'web.qunit_mobile_suite_tests': [
        #     'web_mobile/static/tests/*_mobile_tests.js',
        # ],
    },
    # 'installable': True,
    # 'auto_install': True,
    'license': 'LGPL-3',
}
