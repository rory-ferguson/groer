from django.db import models


class OpenPayments(models.Model):
    """ DB models for openpayments dataset
        Contains 65 Datatypes listed on https://openpaymentsdata-origin.cms.gov/dataset/General-Payment-Data-Detailed-Dataset-2015-Reporti/8xjh-6p62
    """
    change_type = models.CharField(max_length=255, blank=True, null=False)
    covered_recipient_type = models.CharField(max_length=255, blank=True, null=False)
    teaching_hospital_ccn = models.CharField(max_length=255, blank=True, null=False)
    teaching_hospital_id = models.CharField(max_length=255, blank=True, null=False)
    teaching_hospital_name = models.CharField(max_length=255, blank=True, null=False)
    physician_profile_id = models.CharField(max_length=255, blank=True, null=False)
    physician_first_name = models.CharField(max_length=255, blank=True, null=False)
    physician_middle_name = models.CharField(max_length=255, blank=True, null=False)
    physician_last_name = models.CharField(max_length=255, blank=True, null=False)
    physician_name_suffix = models.CharField(max_length=255, blank=True, null=False)
    recipient_primary_business_street_address_line1 = models.CharField(max_length=255, blank=True, null=False)
    recipient_primary_business_street_address_line2 = models.CharField(max_length=255, blank=True, null=False)
    recipient_city = models.CharField(max_length=255, blank=True, null=False)
    recipient_state = models.CharField(max_length=255, blank=True, null=False)
    recipient_zip_code = models.CharField(max_length=255, blank=True, null=False)
    recipient_country = models.CharField(max_length=255, blank=True, null=False)
    recipient_province = models.CharField(max_length=255, blank=True, null=False)
    recipient_postal_code = models.CharField(max_length=255, blank=True, null=False)
    physician_primary_type = models.CharField(max_length=255, blank=True, null=False)
    physician_specialty = models.CharField(max_length=255, blank=True, null=False)
    physician_license_state_code1 = models.CharField(max_length=255, blank=True, null=False)
    physician_license_state_code2 = models.CharField(max_length=255, blank=True, null=False)
    physician_license_state_code3 = models.CharField(max_length=255, blank=True, null=False)
    physician_license_state_code4 = models.CharField(max_length=255, blank=True, null=False)
    physician_license_state_code5 = models.CharField(max_length=255, blank=True, null=False)
    submitting_applicable_manufacturer_or_applicable_gpo_name = models.CharField(max_length=255, blank=True, null=False)
    applicable_manufacturer_or_applicable_gpo_making_payment_id = models.CharField(max_length=255, blank=True, null=False)
    applicable_manufacturer_or_applicable_gpo_making_payment_name = models.CharField(max_length=255, blank=True, null=False)
    applicable_manufacturer_or_applicable_gpo_making_payment_state = models.CharField(max_length=255, blank=True, null=False)
    applicable_manufacturer_or_applicable_gpo_making_payment_country = models.CharField(max_length=255, blank=True, null=False)
    total_amount_of_payment_usdollars = models.CharField(max_length=255, blank=True, null=False)
    date_of_payment = models.CharField(max_length=255, blank=True, null=False)
    number_of_payments_included_in_total_amount = models.CharField(max_length=255, blank=True, null=False)
    form_of_payment_or_transfer_of_value = models.CharField(max_length=255, blank=True, null=False)
    nature_of_payment_or_transfer_of_value = models.CharField(max_length=255, blank=True, null=False)
    city_of_travel = models.CharField(max_length=255, blank=True, null=False)
    state_of_travel = models.CharField(max_length=255, blank=True, null=False)
    country_of_travel = models.CharField(max_length=255, blank=True, null=False)
    physician_ownership_indicator = models.CharField(max_length=255, blank=True, null=False)
    third_party_payment_recipient_indicator = models.CharField(max_length=255, blank=True, null=False)
    name_of_third_party_entity_receiving_payment_or_transfer_of_value = models.CharField(max_length=255, blank=True, null=False)
    charity_indicator = models.CharField(max_length=255, blank=True, null=False)
    third_party_equals_covered_recipient_indicator = models.CharField(max_length=255, blank=True, null=False)
    contextual_information = models.CharField(max_length=255, blank=True, null=False)
    delay_in_publication_indicator = models.CharField(max_length=255, blank=True, null=False)
    record_id = models.CharField(max_length=255, blank=True, null=False)
    dispute_status_for_publication = models.CharField(max_length=255, blank=True, null=False)
    product_indicator = models.CharField(max_length=255, blank=True, null=False)
    name_of_associated_covered_drug_or_biological1 = models.CharField(max_length=255, blank=True, null=False)
    name_of_associated_covered_drug_or_biological2 = models.CharField(max_length=255, blank=True, null=False)
    name_of_associated_covered_drug_or_biological3 = models.CharField(max_length=255, blank=True, null=False)
    name_of_associated_covered_drug_or_biological4 = models.CharField(max_length=255, blank=True, null=False)
    name_of_associated_covered_drug_or_biological5 = models.CharField(max_length=255, blank=True, null=False)
    ndc_of_associated_covered_drug_or_biological1 = models.CharField(max_length=255, blank=True, null=False)
    ndc_of_associated_covered_drug_or_biological2 = models.CharField(max_length=255, blank=True, null=False)
    ndc_of_associated_covered_drug_or_biological3 = models.CharField(max_length=255, blank=True, null=False)
    ndc_of_associated_covered_drug_or_biological4 = models.CharField(max_length=255, blank=True, null=False)
    ndc_of_associated_covered_drug_or_biological5 = models.CharField(max_length=255, blank=True, null=False)
    name_of_associated_covered_device_or_medical_supply1 = models.CharField(max_length=255, blank=True, null=False)
    name_of_associated_covered_device_or_medical_supply2 = models.CharField(max_length=255, blank=True, null=False)
    name_of_associated_covered_device_or_medical_supply3 = models.CharField(max_length=255, blank=True, null=False)
    name_of_associated_covered_device_or_medical_supply4 = models.CharField(max_length=255, blank=True, null=False)
    name_of_associated_covered_device_or_medical_supply5 = models.CharField(max_length=255, blank=True, null=False)
    program_year = models.CharField(max_length=255, blank=True, null=False)
    payment_publication_date = models.CharField(max_length=255, blank=True, null=False)
