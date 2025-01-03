# app/db.py

# Simulate fetching invoices (you can replace this with actual DB logic)
def get_invoices():
    # Replace this with actual database query or data fetching logic
    return [
        {
            "id": 58820,
            "previous_requisition_id": 58819,
            "project_id": 789,
            "billing_date": "2013-11-20",
            "created_at": "2013-11-15T12:00:00Z",
            "updated_at": "2013-11-15T12:00:00Z",
            "commitment_id": 701973,
            "commitment_type": "WorkOrderContract",
            "contract_name": "Contract SC-001",
            "deletable": False,
            "final": True,
            "vendor_name": "Ernie's Electrical",
            "vendor_id": 8881212,
            "invoice_number": 123,
            "origin_data": "XYZ-0012",
            "origin_id": "abc-123",
            "payment_date": "2013-11-15",
            "percent_complete": 0,
            "period_id": 4293,
            "requisition_start": "2013-11-01",
            "requisition_end": "2013-11-02",
            "status": "approved",
            "erp_status": "synced",
            "number": 1,
            "submitted_at": "2013-11-02",
            "total_claimed_amount": "100.00",
            "electronic_signature_id": 701973,
            "move_materials_to_previous_work_completed": False,
            "summary_text": {
                "project_name": "Project",
                "project_number": "100",
                "to_general_contractor": "Company A",
                "requisition_period_start": "2010-01-01",
                "requisition_period_end": "2010-01-01",
                "subcontractor_name": "Company B",
                "subcontractor_street": "101 XYZ Avenue",
                "subcontractor_city": "New York",
                "subcontractor_state_code": "NY",
                "subcontractor_zip": "10101",
                "subcontractor_country_code": "US",
                "application_number": "1",
                "contract_for": "Ceiling Tiles",
                "contract_date": "2010-01-01"
            },
            "summary": {
                "balance_to_finish_including_retainage": 1268346.55,
                "completed_work_retainage_percent": 10,
                "completed_work_retainage_amount": "1201.0",
                "contract_sum_to_date": 1279159.15,
                "current_payment_due": 10812.6,
                "formatted_period": "01/06/19 - 30/06/19",
                "less_previous_certificates_for_payment": 0,
                "negative_change_order_item_total": 0,
                "negative_new_change_order_item_total": 0,
                "negative_previous_change_order_item_total": 0,
                "net_change_by_change_orders": 256706.65,
                "original_contract_sum": 1022452.5,
                "positive_change_order_item_total": "0.00",
                "positive_new_change_order_item_total": "0.00",
                "positive_previous_change_order_item_total": "0.00",
                "stored_materials_retainage_amount": 0.4,
                "stored_materials_retainage_percent": 10,
                "tax_applicable_to_this_payment": 0,
                "total_completed_and_stored_to_date": 1201.4,
                "total_earned_less_retainage": 10812.6,
                "total_retainage": 1201.4,
                "new_materials": "1975.31",
                "new_materials_quantity": "98.7654",
                "stored_materials": "716.05",
                "stored_materials_quantity": "35.80249"
            },
            "created_by": {
                "id": 1738090,
                "name": "John Doe",
                "login": "johndoe@example.com",
                "company_name": "Builders Inc."
            },
            "custom_fields": {
                "custom_field_%{custom_field_string_definition_id}": {
                    "data_type": "string",
                    "value": "custom field value"
                },
                "custom_field_%{custom_field_decimal_definition_id}": {
                    "data_type": "decimal",
                    "value": 2.2
                },
                "custom_field_%{custom_field_boolean_definition_id}": {
                    "data_type": "boolean",
                    "value": True
                },
                "custom_field_%{custom_field_lov_entry_definition_id}": {
                    "data_type": "lov_entry",
                    "value": {
                        "id": 1,
                        "label": "Open"
                    }
                },
                "custom_field_%{custom_field_lov_entries_definition_id}": {
                    "data_type": "lov_entries",
                    "value": [
                        {
                            "id": 2,
                            "label": "Open"
                        }
                    ]
                }
            },
            "currency_configuration": {
                "currency_iso_code": "USD",
                "currency_exchange_rate": 1.8,
                "base_currency_iso_code": "EUR"
            },
            "attachments": [
                {
                    "id": 5324,
                    "url": "http://www.example.com/",
                    "filename": "january_receipt_copy.jpg",
                    "content_type": "image/jpeg"
                }
            ],
            "items": [
                {
                    "id": 341256,
                    "item_type": "contract_detail_item",
                    "accounting_method": "amount",
                    "cost_code_id": 21585118,
                    "currency_configuration": {
                        "currency_iso_code": "USD",
                        "currency_exchange_rate": 1.8,
                        "base_currency_iso_code": "EUR"
                    },
                    "line_item_id": 3129856,
                    "description_of_work": "Install windows",
                    "net_amount": "100.00",
                    "gross_amount": "200.00",
                    "wbs_code": {
                        "id": 44,
                        "flat_code": "2.E",
                        "description": "Earthwork.Equipment",
                        "segment_items": [
                            {
                                "id": 55,
                                "code": 2,
                                "name": "Earthwork",
                                "path_ids": [
                                    [55]
                                ],
                                "path_codes": [
                                    ["2 - Earthwork"]
                                ],
                                "segment_type": "cost_code",
                                "segment_id": 42
                            }
                        ]
                    },
                    "scheduled_value": "1.00",
                    "work_completed_from_previous_application": "0.00",
                    "work_completed_this_period": "0.00",
                    "materials_presently_stored": "2691.36",
                    "materials_presently_stored_quantity": "134.56789",
                    "materials_presently_stored_from_previous_progress": "0.00",
                    "materials_previously_stored_quantity": 12.3456,
                    "materials_moved": "0.00",
                    "materials_retainage_retained_moved": "0.00",
                    "total_completed_and_stored_to_date": "0.00",
                    "total_completed_and_stored_to_date_percent": "0.0",
                    "total_completed_and_stored_to_date_from_previous": "100.00",
                    "work_completed_retainage_from_previous_application": "0.0",
                    "work_completed_retainage_retained_this_period": "0.0",
                    "work_completed_retainage_percent_this_period": "10.0",
                    "materials_stored_retainage_currently_retained": "0.0",
                    "materials_stored_retainage_percent_this_period": "10.0",
                    "materials_stored_retainage_new_materials": "10.0",
                    "work_completed_retainage_released_this_period": "0.0",
                    "materials_stored_retainage_released_this_period": "0.0",
                    "scheduled_quantity": "0.0",
                    "scheduled_unit_price": "20.0",
                    "work_completed_this_period_quantity": "0.0",
                    "work_completed_from_previous_application_quantity": "0.0",
                    "comment": "Installation charges",
                    "status": "no_action",
                    "position": 1,
                    "line_number": "1.1",
                    "ssr_manual_override": False,
                    "subcontractor_claimed_amount": "0.0"
                }
            ]
        }
    ]
