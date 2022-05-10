```
mutation update_attendance($rfid_key: String, $changes: attendance_entry_set_input) {
  update_attendance_entry(where: {rfid_key: {_lte: $rfid_key}},
  _set: $changes) {
    affected_rows 
    returning{
      id
      in_time
      out_time
    }
  }
}


{
    "rfid_key": "0008865576",
    "changes": {
        "out_time": "2012-04-21T18:25:43-05:00"
    }
}
```