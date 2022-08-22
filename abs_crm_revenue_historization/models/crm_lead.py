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
from odoo import api, fields, models,_
from datetime import datetime

class CrmLead(models.Model):
    _inherit = "crm.lead"

    revenue_estimation_ids = fields.One2many('crm.revenue.estimation','opprtunity_id',string='Revenue Estimation')

   
    def write(self, vals):
        flag= False
        estimated_revenue_obj = self.env['crm.revenue.estimation']
        if vals.get('planned_revenue',False):
            plan_revenue = vals['planned_revenue']
            flag = True
        else:
            plan_revenue = self.expected_revenue

        if vals.get('probability',False):
            probability_new = vals['probability']
            flag = True
        else:
            probability_new = self.probability

        if flag:
            values = {'opprtunity_id':self.id, 'planned_revenue': plan_revenue, 'probability': probability_new, 'planned_date': fields.datetime.now(), 'stage_id': self.stage_id.id, 'user_id':self.user_id.id, 'team_id':self.team_id.id, 'date_deadline':self.date_deadline, 'updated_by_id':self.env.uid} 
            estimated_revenue_obj.create(values)

        return super(CrmLead, self).write(vals)
