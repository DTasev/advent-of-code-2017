
STORE = 0
OPERATION = 1
VALUE = 2
REGISTER = 4
COMPARISON = 5
VAR = 6


def main
    data = IO.readlines('input')
    data.map! {|line| line.split ' '}

    # this must use the => syntax, otherwise ruby converts it to a symbol
    operators = {"inc"=> :+, "dec"=> :-}
    # initialise a new entry, if the requested hash is not present
    registers = Hash.new { |hash, key| hash[key] = 0 }

    highest_ever = -100000

    data.each do |line|
        print line
        puts
        # make sure we always have the variable in the register, but add as we go
        register_name = line[REGISTER]
        storage_name = line[STORE]

        register = registers[register_name]
        
        if register.send(line[COMPARISON], line[VAR].to_i)
            registers[storage_name] = registers[storage_name].send(operators[line[OPERATION]], line[VALUE].to_i)
        end
        current_max_val = registers.values.max
        if current_max_val > highest_ever
            highest_ever =current_max_val
        end
    end
    puts registers
    puts registers.values.max
    puts highest_ever
end

main