#### encryption example
- convert a file into base64 string (encoding)
- encrypt the base64 string with sha256 and yeild a 64-char long hash
- decode the base64 string and comply it back to a chunk file then name it with sha256 hash plus i0 pointer
#### demonstration purpose
it is not an ordinal ID since you will always receive the same hash with the same file; if you want to inscribe the same file twice, you cannot make it; instead, you should consider adding a counter, i.e., time-based or object-based, to comply another one with an non-repeated number, i.e, inscription ID, to yeild an unique ID
