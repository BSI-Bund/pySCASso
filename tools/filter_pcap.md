Tshark can be used to produce filtered pcap files which are smaller and could only contain packets relevant to a specific test case.

Only save packets containing "Security Mode Complete" messages:

```
tshark -2 -r open5gs_attach.pcap -w open5gs_attach_filtered.pcap -R "nas_5gs.mm.message_type == 0x5e"
```

Only save packets that contain the ngap protocol (here we pass an option to tshark to decode some extra layers if available):

```
tshark -2 -r open5gs_attach.pcap -w open5gs_attach_filtered.pcap -R "ngap" -o "nas-5gs.null_decipher":"TRUE"
```
