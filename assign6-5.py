text = "X-DSPAM-Confidence:    0.8475"
fdata=text.find('0')
exdata=text[fdata:]
nexdata=float(exdata)
print(nexdata)
