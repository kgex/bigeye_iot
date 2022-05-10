## update mutation
```
mutation update_attendance($out_time: timestamp, $id: Int!) {
  update_attendance_entry_by_pk(pk_columns:{ id: $id}
  _set: {out_time: $out_time}) {
      id
      in_time
      out_time
  }
}

{
    id
    out_time
}

```