# Constants
DATADIR = '../data/'
TOTAL_FIELDS = 259

def read_csv(fname):
    fin = open(fname, 'r')
    fdata = fin.read()
    fin.close
    return fdata

def write_csv(fname, data):
    print('writing', fname)
    fout = open(fname, 'w')
    fout.write(data)
    fout.close()

def get_gas_table():
    gas_price_data = read_csv(DATADIR + 'gas_table.csv').split('\n')[:-1]
    
    gas_table = {}
    for d in gas_price_data:
        fields = d.split(',')
        gas_table[fields[0]] = {
            'current_gas_cost': fields[1],
            'proposed_gas_cost': fields[2],
            'mnemonic': fields[3],
        }
    return gas_table

def convert_to_csv(data):
    out_str = ''
    for line in data:
        out_str += ','.join(line) + '\n'
    return out_str

gas_table = get_gas_table()

csv_data = read_csv('../data/histogram_2.csv').split('\n')

header = csv_data[:2]
data = csv_data[2:]

opnames = csv_data[0].split(',')
opnums  = csv_data[1].split(',')

output_data = []

for dt in data:
    # Calculate using current cost
    fields = dt.split(',')
    
    # Ignore empty or truncated lines
    if len(fields) != TOTAL_FIELDS:
        continue
    
    # Ignore lines containing just 0s
    block_number = fields[0]
    block_gas_usage = fields[1]
    
    if block_number == "0":
        continue
    
    block_total = 0
    block_new_total = 0
    
    # For the opcodes in the gas table:
    # - get the total of gas used
    # - get the total of gas used with new pricings
    # - get the difference
    ix = 2
    for count in fields[2:]:
        opnum = opnums[ix]
        opname = opnames[ix]
        
        if opnum in gas_table.keys():
            cost = gas_table[opnum]['current_gas_cost']
            total = int(count) * int(cost)
            new_cost = gas_table[opnum]['proposed_gas_cost']
            new_total = int(count) * int(new_cost)
            
            block_total += total
            block_new_total += new_total      
        ix += 1

    # Substracts the difference from the initial block's gas used
    diff = block_total - block_new_total
    new_block_gas_usage = int(block_gas_usage) - diff
        
    # Calculate the % decreased
    decrease = int(block_gas_usage) - new_block_gas_usage
    
    try:
        decrease_perc = (decrease / float(block_gas_usage)) * 100
    except:
        print('>>> ignoring block', block_number, '(gasUsed = ', block_gas_usage, ')')
        continue   
    
    # Collect new results including new_block_gas_usage, decrease and %
    data_line = [block_number, block_gas_usage, str(new_block_gas_usage), str(decrease), "{:.4f}".format(decrease_perc) + '%'] + fields[2:]
    output_data.append(data_line)

output_csv = convert_to_csv(output_data)
write_csv(DATADIR + 'histogram_result.csv', output_csv)

