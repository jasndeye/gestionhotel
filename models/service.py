from email.mime import image
from email.policy import default
from odoo import models,fields,api

class Service(models.Model):
     _name = 'hotel.service'

     nom=fields.Char(string="Chambre")
     image= fields.Binary(string="Photo")
     description= fields.Text(string="description")
     tarif_horaire= fields.Float(string="Tarif horaire")