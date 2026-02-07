# Weight Tracker

## Instructions

Get your client ID and secret from https://dev.fitbit.com/apps. Add them to the `.env` file.

Run `./gather_keys_oauth2.py` using your client ID and secret. Add the access token and refresh token to the `.env` file.

Run `./weight_tracker.py` to get your weight data for the last 7 days. Supply a date in the format YYYY-MM-DD or leave blank for today's date.
