# -*- coding: utf-8 -*-
#################################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2022-today Ascetic Business Solution <www.asceticbs.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#################################################################################

from odoo import api, fields, models, _

class CrmRevenueEstimation(models.Model):
    _name = "crm.revenue.estimation"
    _rec_name = "opprtunity_id"

    opprtunity_id = fields.Many2one('crm.lead', string = 'Opprorunity')
    planned_revenue = fields.Float(string='Expexted Revenue')
    probability = fields.Float(string='Probability')
    planned_date = fields.Datetime(string='Planned Date')
    stage_id = fields.Many2one('crm.stage', string = 'Stage')
    user_id = fields.Many2one('res.users', string = 'Sales Person')
    team_id = fields.Many2one('crm.team', string = 'Sales Team')
    date_deadline = fields.Date(string='Expected Closing')
    updated_by_id = fields.Many2one('res.users', string = 'Updated By')




