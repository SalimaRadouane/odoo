# -*- coding: utf-8 -*-


from odoo import _,models, fields, api




class participant(models.Model):
     _name = 'formation.participant'
     _inherit = ['mail.thread', 'mail.activity.mixin']
     _description = 'formation.participant'
     _rec_name = 'name_participant'

     participant_id = fields.Char('Id Participant')
     name_participant = fields.Char('Name')
     niveau_etude = fields.Char('Niveau Etude')
     email_id = fields.Char(string="Email")
     phone = fields.Char('Phone')
     sexe = fields.Selection([('homme', 'Homme'), ('femme', 'Femme')], string="Sexe")
     type = fields.Selection([('individuel', 'Individuel'), ('etudiant', 'Etudiant'), ('société','Société')], string="Type")
     nom_société = fields.Char('Nom Société')
     participant_age = fields.Integer('Age', track_visibility="always", group_operator=False)
     session_formation_id = fields.Many2one('formation.formation', "Session")
     payment_id = fields.One2many('formation.payment', 'participant_id')
     user_id = fields.Many2one('res.users', string="PRO")
     name_seq = fields.Char(string='Participant ID', required=True, copy=False, readonly=True,
                            index=True, default=lambda self: _('New'))
     name = fields.Char(string="Contact Number")
     id = fields.Integer()
     image_1920 = fields.Image("Image")
     sms = fields.Text(string="SMS", required="")
     #borrower_id = fields.Many2one('res.partner', 'Borrower', required=True)

     state = fields.Selection([('ongoing', 'Ongoing'), ('returned', 'Returned')],
                              'State', default='ongoing', required=True)

     color = fields.Integer()
     popularity = fields.Selection(
          [('no', 'No Demand'), ('low', 'Low Demand'), ('medium', 'Average Demand'), ('high', 'High Demand'), ])
     tag_ids = fields.Many2many('participant.tag')

     stage_id = fields.Many2one(
          'participant.stage', string="payment", group_expand='_group_expand_stages'
     )

     @api.model
     def _default_rent_stage(self):
          Stage = self.env['participant.stage']
          return Stage.search([], limit=1)

     @api.model
     def _group_expand_stages(self, stages, domain, order):
          return stages.search([], order=order)

     def action_send_mail(self):
          self.ensure_one()
          template_id = self.env.ref('formation.email_template_participant').id
          ctx = {
               'default_model': 'formation.participant',
               'default_res_id': self.id,
               'default_use_template': bool(template_id),
               'default_template_id': template_id,
               'default_composition_mode': 'comment',
               'email_to': self.email_id,
          }
          return {
               'type': 'ir.actions.act_window',
               'view_type': 'form',
               'view_mode': 'form',
               'res_model': 'mail.compose.message',
               'target': 'new',
               'context': ctx,
          }


     def action_open_payment(self):
          return {
               'type': 'ir.actions.act_window',
               'name': 'Pyaments',
               'res_model': 'formation.payment',
               'view_type': 'form',
               'domain': [('participant_id', '=', self.id)],
               'context': {'default_participant_id': self.id},
               'view_mode': 'tree,form',
               'target': 'current',
          }

     def send_sms(self):
         from twilio.rest import Client

         #Your ACCOUNT SID from twilio
         account_sid = "ACaf4c43b3d27215fb913a5bef6b0b841b"
         #Your Auth Token from twilio.com
         auth_token = "1a086d15ad22a4bd9015cd871a3c2969"

         client = Client(account_sid, auth_token)

         message = client.messages.create(
              body="Cher Nous vous invitons à être présent à la Formation de la semaine prochaine.Meilleures salutations,",
              from_="+19403988751",
              to=self.phone)

     def main(self):
          self.send_sms("Hello from python!")
     if __name__== "__main__":
          main()

          # sending the participant report to participant via email
          #print("sending mail")
          #template_id = self.env.ref('formation.participant_card_email_template').id
          #self.env['mail.template'].browse(template_id).send_mail(self.id, force_send=True)


     #def send_mail(self):


     #@api.constrains('participant_id')
     #def check_participant_id(self):
      #   for rec in self:
       #      participants = self.env['formation.participant'].search([('participant_id', '=', rec.participant_id)])
        #     if participants:
         #        raise ValidationError (_("Id %s Already Exists" % rec.participant_id))









class ParticipantStage(models.Model):
     _name = 'participant.stage'
     _order = 'sequence,name'

     name = fields.Char()
     sequence = fields.Integer()
     fold = fields.Boolean()
     payment_state = fields.Selection(
          [('available', 'Pending'),
           ('borrowed', 'Credited'),
           ('lost', 'Completed')],
          'State', default="available")



class ParticipantTags(models.Model):
    _name = 'participant.tag'

    name = fields.Char()
    color = fields.Integer()


#class ResPartner(models.Model):
 #   _inherit = 'res.partner'

  #  participant_ids = fields.One2many('formation.participant', 'borrower_id')





class payment(models.Model):

     _name = 'formation.payment'
     _description = 'formation.payment'

     payment_id = fields.Char('Id Payment')
     mode_paiement = fields.Selection([('especes', 'Especes'), ('cheque', 'Cheque'), ('bancaires', 'Bancaires')], string="Mode Paiement")
     montant_paye = fields.Integer('Montant Paye')
     date_payement = fields.Datetime(string="Date Payement")
     color = fields.Integer()
     montant_restant = fields.Integer('Montant Restant')
     expected_to_be_payed = fields.Char('Expected to be payed')
     priority = fields.Selection([('0', 'Normal'), ('1', 'Low'), ('2', 'High'), ('3', 'Very High')], string="Priority")

     active = fields.Boolean(string="Active", default=True)

     tag_ids = fields.Integer('Tags')


     participant_id = fields.Many2one('formation.participant', "Participant")

     @api.model
     def _get_Formation_default(self):
          res = self.env['formation.formation'].search([('payment_id', '!=', [])], limit=1)
          return res and res.id or False


     session_formation_id = fields.Many2one('formation.formation', "Session",default=_get_Formation_default)

     @api.model
     def _default_formation(self):
          return self.env['formation.formation'].search([], limit=1).id


     #@api.model
     #def default_get(self, fields):
          #res = super(payment, self).default_get(fields)
          #if self._context.get('active_id'):
               #res['session_formation_id'] = self._context.get('active_id')
          #return res