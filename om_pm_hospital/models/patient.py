# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient Record'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age', required=False)
    is_child= fields.Boolean(string='Is Child ?')
    gender = fields.Selection([('male','Male'),('female','Female'),('other','Other')], string='Gender', required=True)