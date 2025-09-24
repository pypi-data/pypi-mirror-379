import logging
from django.db.models import ForeignKey
from rest_framework import serializers

logger = logging.getLogger(__name__)


class BulkModelSerializer(serializers.ModelSerializer):
    """
    Bulk-optimized serializer that accepts standard Django field names and converts
    them internally for optimal bulk operation performance.

    Key features:
    - Accepts standard field names (loan_account) in API requests
    - Converts to *_id fields internally for bulk_create/bulk_update efficiency
    - Returns standard field names in responses for consistency
    - Full django-filter compatibility
    - Avoids foreign key validation queries during bulk operations
    """

    def to_internal_value(self, data):
        """
        Convert standard foreign key field names to *_id fields for bulk operations.

        Example:
        Input:  {"loan_account": 123, "amount": 1000}
        Output: {"loan_account_id": 123, "amount": 1000}

        This allows users to work with familiar Django field names while optimizing
        the internal representation for bulk database operations.
        """
        # Make a copy to avoid modifying the original data
        internal_data = data.copy() if hasattr(data, "copy") else dict(data)

        model = self.Meta.model

        # Process all foreign key fields
        for model_field in model._meta.get_fields():
            if not isinstance(model_field, ForeignKey):
                continue

            fk_name = model_field.name  # e.g., 'business'
            fk_attname = model_field.attname  # e.g., 'business_id'

            # Debug logging
            logger.debug(f"BulkModelSerializer - Found FK field '{fk_name}' -> '{fk_attname}' in data keys: {list(internal_data.keys())}")

            # Convert standard field name to _id field if present
            if fk_name in internal_data and fk_attname not in internal_data:
                # Move the value from business to business_id
                internal_data[fk_attname] = internal_data.pop(fk_name)
                logger.info(f"BulkModelSerializer - Converted '{fk_name}': {internal_data[fk_attname]} -> '{fk_attname}'")

        logger.info(f"BulkModelSerializer - Final internal_data: {internal_data}")
        return super().to_internal_value(internal_data)
