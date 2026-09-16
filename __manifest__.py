{
    "name": "Insurance Profit and Loss",
    "version": "19.0.1.0.0",
    "category": "Accounting",
    "summary": "Custom dynamic Profit and Loss report for Insurance logic",
    "author": "Havano",
    "license": "LGPL-3",
    "depends": [
        "base",
        "account",
        "account_reports",
    ],
    "data": [
        "views/account_account_views.xml",
        "views/res_config_settings_views.xml",
        "data/insurance_profit_and_loss.xml",
        "data/dynamic_reports_action.xml",
    ],
    "installable": True,
    "application": False,
}
