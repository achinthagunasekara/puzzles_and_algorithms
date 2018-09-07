# Find Unique People

Given an array of contacts with phone/emails, detect and union identical contacts.

## Example

```
Contacts array:
[ [ "John", "john@gmail.com", "john@linkedin.com"],
[ "Dan", "dan@gmail.com", "+1234567"],
[ "john123", "+5412312", "john123@skype.com"],
[ "john1985", "+5412312", "john@linkedin.com"] ]
```

We can see that john1985, John and john123 are the same person by their contact information.

### Output

0,2,3 are the same person and 1 is another one

[[ 0, 2, 3], [1]]
