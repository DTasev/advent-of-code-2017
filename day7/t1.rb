data = IO.readlines("input")
nodes = Hash.new {|hash, key| hash[key] = {children: [], parent: nil}}
data.map! {|line| line.delete(',').split(' ')}
data.each do |line|
    parent = nodes[line[0]]
    # this node has children
    if line.length > 3
        line.drop(3). each do |child|
            child = nodes[child]
            child[:parent] = parent
            parent[:children].push(child)
         end
    end
end
print nodes.find {|k, v| v[:parent].nil?}.first