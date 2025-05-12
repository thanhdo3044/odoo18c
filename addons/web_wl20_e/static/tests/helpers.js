/** @odoo-module */

import { createWebClient } from "@web/../tests/webclient/helpers";
import { WebClientEnterprise } from "@web_wl20_e/webclient/webclient";

export function createEnterpriseWebClient(params) {
    params.WebClientClass = WebClientEnterprise;
    return createWebClient(params);
}
