from odoo import models,fields,api

class Reservation(models.Model):
     _name = 'hotel.reservation'
     
     date_deb=fields.Datetime(string="Date de Debut")
     date_fin=fields.Datetime(string="Date de Fin")
     prix=fields.Float(string="Prix de la reservation")
     etat=fields.Selection([('r','reservé'),('v','validé'),('t','ternimé'),('a','annulé')], string="Etat de la réservation")
     chambre_ids=fields.Many2many('hotel.chambre', string='Chambres')