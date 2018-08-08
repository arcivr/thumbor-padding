Thumbor Padding
===

This plugin provides a way to pad in an image via Thumbor Filter.

## Installation
`pip install thumbor_padding`

## Configuration

By adding `FILTERS` in `thumbor.conf` with `thumbor_padding_filter`, for example:
```
FILTERS =     [
    # other filters....
    'thumbor_padding_filter',
]
```

## Usage
Add `padding()` to thumbor url at `filters` section, method signature is like this:

`padding(<left>, <top>, <right>, <bottom> [, <color>])`

You can omit `color`, it will use be transparent as default.
For `color`, use a valid hex code __without the #__.

Here are some examples:
```
http://thumbor/unsafe/filters:padding(10, 10, 20, 20)/your-image-url
http://thumbor/unsafe/filters:padding(10, 10, 20, 20, eee)/your-image-url
```

---
## Copyright
MIT
