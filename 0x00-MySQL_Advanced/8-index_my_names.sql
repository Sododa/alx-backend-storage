--      Only the first letter of name must be indexed
CREATE INDEX idx_name_first ON names(name(1));
