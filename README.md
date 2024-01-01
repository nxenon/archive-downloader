# Archive.org Bulk Downloader
Download list of old archived JS URLs from Archive.org that are not available on the application anymore.

# Usage
    python3 archive-downloader.py --urls-file urls.txt --timeout 5.0 --sleep 1.0 --block-sleep 30.0

## Get List of Files from a Domain

    https://web.archive.org/cdx/search/cdx?url=*.example.com/*&output=txt&fl=original&collapse=urlkey

## Example of urls.txt

    https://example.com/some_old_js/that/is_not_served/by/server/anymore.js
    https://example.com/some_old_js/that/is_not_served/by/server/anymore2.js
    .
    .
    .

## Output Example

    Created file: downloads/2024-01-01-15-57/others.js from url: https://statics.REDACTED.com/lib/2.0.31.19/js/others.js
    Created file: downloads/2024-01-01-15-57/angularmore.js from url: https://statics.REDACTED.com/lib/2.0.31.2/js/angularmore.js
    Created file: downloads/2024-01-01-15-57/bootstrap.js from url: https://statics.REDACTED.com/lib/2.0.31.2/js/bootstrap.js
    Created file: downloads/2024-01-01-15-57/jqueryui.js from url: https://statics.REDACTED.com/lib/2.0.31.2/js/jqueryui.js
    Created file: downloads/2024-01-01-15-57/justangular.js from url: https://statics.REDACTED.com/lib/2.0.31.2/js/justangular.js
    Created file: downloads/2024-01-01-15-57/justjquery.js from url: https://statics.REDACTED.com/lib/2.0.31.2/js/justjquery.js
    Created file: downloads/2024-01-01-15-57/others.js from url: https://statics.REDACTED.com/lib/2.0.31.2/js/others.js
    Created file: downloads/2024-01-01-15-57/angularmore.js from url: https://statics.REDACTED.com/lib/2.0.31.20/js/angularmore.js
    Created file: downloads/2024-01-01-15-57/bootstrap.js from url: https://statics.REDACTED.com/lib/2.0.31.20/js/bootstrap.js
    Created file: downloads/2024-01-01-15-57/jqueryui.js from url: https://statics.REDACTED.com/lib/2.0.31.20/js/jqueryui.js
    Created file: downloads/2024-01-01-15-57/justangular.js from url: https://statics.REDACTED.com/lib/2.0.31.20/js/justangular.js
    Created file: downloads/2024-01-01-15-57/justjquery.js from url: https://statics.REDACTED.com/lib/2.0.31.20/js/justjquery.js
    Created file: downloads/2024-01-01-15-57/others.js from url: https://statics.REDACTED.com/lib/2.0.31.20/js/others.js
    .
    .
    .


# Help

    python3 archive-downloader.py --help
    Usage:  python3 archive-downloader.py [Input] [Arguments]

    Input Arguments:
      --urls              url addresses to download JS files from URL or URLs
      --urls-file         name of the file which URLs are in it

    Config Arguments:
      --timeout           timeout for GET requests [default 3.0 SECs: 3.0]
      --sleep             sleep between each request before sending [default 1.0 SECs: 1.0]
      --block-sleep       sleep after the request that got blocked [default 60.0 SECs: 60.0]

    Help:
      --help              print help message

    Examples:
      --urls https://example.com/1.js https://example.com/2.js --timeout 2.0
      --urls-file urls.txt --timeout 1.5 --sleep 5.0
