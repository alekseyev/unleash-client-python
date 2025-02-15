from chainmap import ChainMap
from datetime import datetime
import pytz
import fcache
from UnleashClient.api import send_metrics
from UnleashClient.constants import METRIC_LAST_SENT_TIME


def aggregate_and_send_metrics(url,
                               app_name,
                               instance_id,
                               custom_headers,
                               custom_options,
                               features,
                               ondisk_cache
                               ):
    feature_stats_list = []

    for feature_name in features.keys():
        feature_stats = {
            features[feature_name].name: {
                "yes": features[feature_name].yes_count,
                "no": features[feature_name].no_count
            }
        }

        features[feature_name].reset_stats()
        feature_stats_list.append(feature_stats)

    metrics_request = {
        "appName": app_name,
        "instanceId": instance_id,
        "bucket": {
            "start": ondisk_cache[METRIC_LAST_SENT_TIME].isoformat(),
            "stop": datetime.now(pytz.utc).isoformat(),
            "toggles": dict(ChainMap(*feature_stats_list))
        }
    }

    send_metrics(url, metrics_request, custom_headers, custom_options)
    ondisk_cache[METRIC_LAST_SENT_TIME] = datetime.now(pytz.utc)
    ondisk_cache.sync()
