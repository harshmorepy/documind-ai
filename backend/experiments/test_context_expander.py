from backend.app.context_expander import group_chunk_ranges


sample_metadata = [
    {"chunk_number": 50},
    {"chunk_number": 51},
    {"chunk_number": 52},
    {"chunk_number": 60},
    {"chunk_number": 61},
    {"chunk_number": 90},
]

ranges = group_chunk_ranges(sample_metadata)

print("Detected Ranges:")
print(ranges)