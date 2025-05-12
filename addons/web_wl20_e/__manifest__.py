# -*- coding: utf-8 -*-

{
    'name': 'Web wl20_e',
    'category': 'Website/Website WL20',
    'version': '18.0.0.0',
    'description': """
        """,
    'depends': ['web', 'base_setup'],
    'assets': {
        'web._assets_primary_variables': [
            ('after', 'web/static/src/scss/primary_variables.scss', 'web_wl20_e/static/src/**/*.variables.scss'),
            ('before', 'web/static/src/scss/primary_variables.scss', 'web_wl20_e/static/src/scss/primary_variables.scss'),
        ],
        'web._assets_secondary_variables': [
            ('before', 'web/static/src/scss/secondary_variables.scss', 'web_wl20_e/static/src/scss/secondary_variables.scss'),
        ],
        'web._assets_backend_helpers': [
            ('before', 'web/static/src/scss/bootstrap_overridden.scss', 'web_wl20_e/static/src/scss/bootstrap_overridden.scss'),
        ],
        'web.assets_frontend': [
            'web_wl20_e/static/src/webclient/home_menu/home_menu_background.scss', # used by login page
            'web_wl20_e/static/src/webclient/navbar/navbar.scss',
        ],
        'web.assets_backend': [
            'web_wl20_e/static/src/webclient/**/*.scss',
            'web_wl20_e/static/src/views/**/*.scss',

            'web_wl20_e/static/src/core/**/*',
            'web_wl20_e/static/src/webclient/**/*.js',
            ('after', 'web/static/src/views/list/list_renderer.xml', 'web_wl20_e/static/src/views/list/list_renderer_desktop.xml'),
            'web_wl20_e/static/src/webclient/**/*.xml',
            'web_wl20_e/static/src/views/**/*.js',
            'web_wl20_e/static/src/views/**/*.xml',
            ('remove', 'web_wl20_e/static/src/views/pivot/**'),

            # Don't include dark mode files in light mode
            ('remove', 'web_wl20_e/static/src/**/*.dark.scss'),
        ],
        'web.assets_backend_lazy': [
            'web_wl20_e/static/src/views/pivot/**',
        ],
        'web.assets_backend_lazy_dark': [
            ('include', 'web.dark_mode_variables'),
            # web._assets_backend_helpers
            ('before', 'web_wl20_e/static/src/scss/bootstrap_overridden.scss', 'web_wl20_e/static/src/scss/bootstrap_overridden.dark.scss'),
            ('after', 'web/static/lib/bootstrap/scss/_functions.scss', 'web_wl20_e/static/src/scss/bs_functions_overridden.dark.scss'),
        ],
        'web.assets_web': [
            ('replace', 'web/static/src/main.js', 'web_wl20_e/static/src/main.js'),
        ],
        # ========= Dark Mode =========
        "web.dark_mode_variables": [
            # web._assets_primary_variables
            ('before', 'web_wl20_e/static/src/scss/primary_variables.scss', 'web_wl20_e/static/src/scss/primary_variables.dark.scss'),
            ('before', 'web_wl20_e/static/src/**/*.variables.scss', 'web_wl20_e/static/src/**/*.variables.dark.scss'),
            # web._assets_secondary_variables
            ('before', 'web_wl20_e/static/src/scss/secondary_variables.scss', 'web_wl20_e/static/src/scss/secondary_variables.dark.scss'),
        ],
        "web.assets_web_dark": [
            ('include', 'web.dark_mode_variables'),
            # web._assets_backend_helpers
            ('before', 'web_wl20_e/static/src/scss/bootstrap_overridden.scss', 'web_wl20_e/static/src/scss/bootstrap_overridden.dark.scss'),
            ('after', 'web/static/lib/bootstrap/scss/_functions.scss', 'web_wl20_e/static/src/scss/bs_functions_overridden.dark.scss'),
            # assets_backend
            'web_wl20_e/static/src/**/*.dark.scss',
        ],
        # 'web.tests_assets': [
        #     'web_wl20_e/static/tests/*.js',
        # ],
        # "web.assets_tests": [
        #     "web_wl20_e/static/tests/tours/**/*.js",
        # ],
        # Unit test files
        # 'web.assets_unit_tests': [
        #     'web_wl20_e/static/tests/**/*.test.js',
        # ],
        # 'web.qunit_suite_tests': [
        #     'web_wl20_e/static/tests/views/**/*.js',
        #     'web_wl20_e/static/tests/webclient/**/*.js',
        #     ('remove', 'web_wl20_e/static/tests/**/*.test.js'),
        # ],
    },
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
    # 'post_init_hook': '_setup_module',
    #'uninstall_hook': '_uninstall_cleanup',
}
