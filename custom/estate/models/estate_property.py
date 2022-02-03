import datetime
from email.policy import default
from lib2to3.pygram import python_symbols
from xml.dom import ValidationErr

from odoo.exceptions import UserError, ValidationError
# import re
# from xml.dom import ValidationErr
from odoo import api, fields, models,_


class EstateProperty(models.Model):
    _name='estate.property'
    _description='This new estate module'

    name = fields.Char() 
    description=fields.Char()
    property_type_id = fields.Many2one("property.type")
    address=fields.Char()

    salesman_id = fields.Many2one('res.users',default=lambda self: self.env.user)
    property_offer_ids=fields.One2many('estate.property.offer','property_id')


    # gender=fields.Selection([('male','Male'),('female','Female')])
    # phone=fields.Char()

    # date use inverse
    start_date = fields.Date(default=lambda self: fields.Datetime.now(),copy=False) 
    stop_date=fields.Date(compute="_duration",inverse="_inverse_days")
    duration=fields.Integer(default=7)  

    # domain new field add
    is_virtual_class=fields.Boolean(string="online book?")

    room_ids=fields.One2many('test.view','room_id')
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(copy=False, readonly=True)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    
    state = fields.Selection([('new', 'New'), ('sold', 'Sold'), ('cancel', 'Cancelled')], default='new')
    image=fields.Image()
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ])
    best_price=fields.Float(compute='_computeOffer', store=True)
    
    postcode=fields.Char()
    



    property_tag_ids=fields.Many2many('property.tag')



    total=fields.Float(compute='_compute_total')
    buyer_id = fields.Many2one('res.partner')


# use kanbanview Addoffer_button action 
    def open_offers(self):
        view_id_all = self.env.ref('estate.estate_property_offer_tree').id
        return {
            "name":"Offers",
            "type":"ir.actions.act_window",
            "res_model":"estate.property.offer",
            "views":[[view_id_all, 'tree']],
            # "res_id": 2,
            "target":"new",
            "domain": [('property_id', '=', self.id)]
            }

    def open_confirm_offers(self):
        print ("\n\ncontext is ::: ", self.env.context)
        view_id_accept = self.env.ref('estate.estate_property_offer_tree').id
        return {
            "name":"Offers",
            "type":"ir.actions.act_window",
            "res_model":"estate.property.offer",
            "views":[[view_id_accept, 'tree']],
            # "res_id": 2,
            # "target":"new",
            "domain": [('property_id', '=', self.id),('status','=','accepted')]
            }

# onchange
    @api.onchange('garden')
    def _onchangegarden(self):
        for record in self:
            if record.garden:
                record.garden_area=10
                record.garden_orientation='north'
            else:
                record.garden_area=0
                record.garden_orientation=None


# Compute methods   
    @api.depends('property_offer_ids.price')
    def _computeOffer(self):
        for record in self:
            max_price = 0 
            for offer in record.property_offer_ids:
                if offer.price > max_price:
                    max_price=offer.price
            record.best_price = max_price
 

            
#inverse methods
    @api.depends('duration')
    def _duration(self):
        for record in self:
            record.stop_date=record.start_date - datetime.timedelta(days=record.duration)

    def _inverse_days(self):
        for record in self:
            a = record.stop_date - record.start_date
            record.duration=a.days


    def action_sold(self):
        # print("\n\n In action sold")
        for record in self:
            if record.state=='cancel':
                raise UserError("Cancel Property cannot be sold")
            record.state = 'sold'
            # return some action 

    def action_cancel(self):
        for record in self:
            if record.state=='sold':
                raise UserError("Sold Property cannot be canceled")
            record.state = 'cancel'

    # Constraints
    # @api.constrains('phone')
    # def check_phon(self):
    #     for rec in self:
    #         if len(rec.phone) >= 11:
    #             raise ValidationError("PhonNumber is only 10 Enter")

    # @api.constrains('postcode')
    # def check_pcode(self):
    #     for rec in self:
    #         if rec.postcode<=25:
    #             raise ValidationError('The postcode must 25 to less')
                     


# Model Traditional Inheritance
class TestModel(models.Model):
    _name='test.model'
    _inherit="estate.property"

    new_field=fields.Text()
    # _inheritas={'estate.property':'property_offer_ids'}

    # property_duration=fields.Many2one('estate.property')
    # property_details=fields.Char()
    
# Model Delegration Inheritance
class TestModelView(models.Model):
    _name="test.view"
    _inherits={'estate.property':'room_id'}
    
    
    room_id=fields.Many2one('estate.property')
    additional_details=fields.Text()


# property_Type class
class PropertyType(models.Model):
    _name='property.type'

    name=fields.Char()
    property_ids=fields.One2many('estate.property','property_type_id')
   
# property_tag class
class Property_tag(models.Model): 
    _name='property.tag'
    _description='views likes'

    name=fields.Char()
    
#_Estate_property_Type_offer class
class EstatePropertyTypeOffer(models.Model):
    _name='estate.property.offer'
    _description='This is property offer'

    price=fields.Float()
    partner_id=fields.Many2one('res.partner')
    property_id=fields.Many2one('estate.property')
    property_type_id=fields.Many2one(related='property_id.property_type_id',store=True)
    status = fields.Selection([('accepted', 'Accepted'),('refuse', 'Refused')])

    total=fields.Float(compute="_compute_total",inverse="_inverse_total")
    amount=fields.Float()



    # @api.depends("amount")
    # def _compute_total(self):
    #     for record in self:
    #         record.total=2.0*record.amount

    # def _inverse_total(self):
    #     for record in self:
    #         record.amount=record.total/2.0
        
    def action_refused(self):
        for record in self:
            record.status = 'refuse'

    def action_accepted(self):
        for record in self:
            record.status = 'accepted'
