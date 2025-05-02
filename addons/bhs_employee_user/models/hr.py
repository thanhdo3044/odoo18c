# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from itertools import count

class CreateUserEmployee(models.Model):
    _inherit = "hr.employee"

    @api.model_create_multi
    def create(self, vals):
        recs = super(CreateUserEmployee, self).create(vals) #tạo ra 1 nvien
        for rec in recs:
            if not rec.user_id and rec.env['res.users'].sudo().search([('login', '=', rec.description)]).id:
                raise ValidationError(_('Mã nhân viên đã tồn tại'))
            elif not rec.user_id:
                # user_partner_id = rec.env['res.partner'].sudo().search([('email', '=', rec.work_email), ('is_company', '=', False)]).id
                user_info = {
                    'name': rec.name,
                    'login': rec.description,
                    'email': rec.work_email,
                    'state': 'active',
                    'partner_id': rec.work_contact_id.id,
                    'lang': 'vi_VN',
                    'notification_type': 'inbox',
                    'tz': 'Asia/Saigon',
                    'password': '1'}
                account = self.env['res.users'].sudo().create(user_info)
                rec.user_id = account.id
                self.env['ir.model.data'].sudo().create({
                    'name': 'res_users_' + rec.description,  # Tên External ID
                    'module': 'res_users',  # Module (có thể là module của bạn)
                    'model': 'res.users',  # Model liên quan
                    'res_id': account.id,  # ID của user mới tạo
                    'noupdate': True,
                })
                self.env['ir.model.data'].sudo().create({
                    'name': 'hr_employee_' + rec.description,  # Tên External ID
                    'module': 'hr_employee',  # Module (có thể là module của bạn)
                    'model': 'hr.employee',  # Model liên quan
                    'res_id': rec.id,  # ID của user mới tạo
                    'noupdate': True,
                })
        return recs


class HrApplicantInherit(models.Model):
    _inherit = 'hr.applicant'

    # work_email = fields.Char(string='Work email')

    def create_employee_from_applicant(self):
        res = super(HrApplicantInherit, self).create_employee_from_applicant()
        res['context']['default_work_email'] = None
        res['context']['default_work_contact_id'] = self.partner_id.id

        return res
