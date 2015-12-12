from bucket_filter.bucket import Bucket
from bucket_filter.condition import ConditionType, BooleanCondition

buckets = {}


def get_bucket(expression):
    key = BooleanCondition.build_key(expression)
    return buckets.get(key, None)

def register_bucket(expression, elements=None, condition_type=ConditionType.BOOLEAN):
    if condition_type == ConditionType.BOOLEAN:
        key = BooleanCondition.build_key(expression)
        if key not in buckets:
            condition = BooleanCondition(expression)
            bucket = Bucket(condition, elements)
            buckets[condition.key] = bucket
