# BSON

- Binary representation of JSON
- Optimized for speed and secutiry
- Prevents JSON injections
- Adds metadata
- Adds new types


### Core Types
1. **String**: Stores text data (UTF-8 encoded).
2. **Integer**: Supports `int32` and `int64`.
3. **Double**: 64-bit floating-point values.
4. **Boolean**: `true` or `false`.
5. **Null**: Represents a null value.
6. **Array**: An ordered list of values.
7. **Embedded Document**: Objects or nested documents.

### Specialized Types
1. **ObjectId**: 12-byte unique identifier.
2. **Date**: Milliseconds since Unix epoch.
3. **Binary Data**: Stores binary-encoded data like images.
4. **Regular Expression**: For pattern matching.
5. **Decimal128**: High-precision decimal for exact numeric operations.
6. **Timestamp**: Special value for internal MongoDB usage.
7. **JavaScript with Scope**: Stores JavaScript code with a scope.