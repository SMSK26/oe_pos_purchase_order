/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { ControlButtons } from "@point_of_sale/app/screens/product_screen/control_buttons/control_buttons";
import { _t } from "@web/core/l10n/translation";

patch(ControlButtons.prototype, {
    clickPurchaseOrder() {
        window.open("/web#model=purchase.order&view_type=form", "_blank");
    },

    get purchaseOrderLabel() {
        return _t("Purchase Order");
    },
});
