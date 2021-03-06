# Copyright 2018 Mikel Arregi Etxaniz - AvanzOSC
# Copyright 2015 Oihane Crucelaegui - AvanzOSC
# Copyright 2015-2016 Pedro M. Baeza <pedro.baeza@tecnativa.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "Product Variants",
    "version": "11.0.2.0.0",
    "depends": [
        "product",
    ],
    "author": "OdooMRP team,"
              "AvanzOSC,"
              "Tecnativa",
    "contributors": [
        "Oihane Crucelaegui <oihanecrucelaegi@avanzosc.es>",
        "Pedro M. Baeza <pedro.baeza@serviciosbaeza.com>",
        "Ana Juaristi <ajuaristio@gmail.com>",
    ],
    "category": "Product Variant",
    "website": "http://www.odoomrp.com",
    "summary": "Disable automatic product variant creation",
    "data": [
        "views/product_attribute_price_view.xml",
        "views/product_category_view.xml",
        "views/product_configurator_view.xml",
        "views/product_product_view.xml",
        "views/product_template_view.xml",
        "security/ir.model.access.csv",
        "security/product_configurator_security.xml",
    ],
    "installable": True,
}
