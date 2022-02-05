{
    'name':"Real Estate",
    'description':'This is my first app',
    'depends':['base',
    'mail',
    'website'
    ],
    'application':True,
    'data':[
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/estate_property_views.xml',
        'views/estate_property_menus.xml',
        'wizard/offer_wizard_view.xml',
        'views/temlates.xml',      

    ],
    'category':'Sales',
}