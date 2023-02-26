-- it selects all the attributes
db.users.find({"personID": 3 }) 

-- it selects the documents personID = 5 and just shows firstname and lastcity of them
db.users.find({"personID": 5}, {firstname: 1, lastcity:1})

{metacritic: {$gte: 50,$lt: 65}} 

{loc: {$geowithin: {$centerSphere : [[123, 321], 154]}}}
{loc: {$geoWithin: { $centerSphere: [ [ 7.643072149898009, 45.048324324219315 ], 0.000018940501236385475 ]}}}

use DataBase
show collections
show databases

--it shows every thing--good for test
db.Parkings.find()

-- you can insert one with _id
db.Parkings.insertOne({_id: 1234, name:"Iman", famName: "Alavi" })

-- you can insert one without  _id it returns a unique id 
db.Parkings.insertOne({ name:"Iman", famName: "Alavi" })

--insert many using lists pay attention to id
db.Parkings.insertMany([{ name:"Imann", famName: "Alavi" },{_id: 1234444 ,name: "Mahdi", famName: "Shahraki"}])

--pay attention to difference
db.Parkings.insertOne({ _id : "1234444",name:"Iman", famName: "Alavi" })
db.Parkings.insertOne({ _id : 1234444,name:"Iman", famName: "Alavi" })


db.createCollection("collectionName", {differentOptions})

db.collectionName.drop()

--nested
db.Parkings.insertOne({fullname: {name:"John", surname:"Bolton"}, city: "newYork"})
-- to store multi media data use grid fs

-- use lists 
db.Parkings.insertOne({_id: 1234655215, name: "jack", favColor: ["blue", "red", 'Yellow']})


--it deletes all the documents which have age = 23
db.Parkings.deleteMany ({age: 23})

-- you can exclude sth in the result by assigning 0
db.Parkings.find({age: "30"}, {name:1, famName: 1, _id: 0})

-- how to access values inside attributes 
db.Bookings.find({"driving.duration": 329})

--access to values inside a list
--{ _id: 251,
 -- name: 'Hossein',
--  age: 22,
  --year: 2021,
--  favColor: [ 'red', 'blue', 'yellow' ] }

db.Parkings.find({favColor: "red"})

-- $in [x, y, z]  value should be x or y or z
db.Bookings.find({init_fuel: 84, city: "Torino", distance:{ $in: [2119,3604,2565] }})

-- init_fuel OR final_fuel
db.Bookings.find({$in: [{init_fuel: 45},{final_fuel: 45}]})

-- distance AND init_fuel at the same time OR distance AND init_fuel at the same time 
db.Bookings.find({$or: [{distance: 346, init_fuel: 52}, {distance: 347, init_fuel: 5212} ]})

--they return the same result
db.Bookings.count({init_fuel: 52, final_fuel: 45})
db.Bookings.find({init_fuel: 52, final_fuel: 45}).count()

--comparison operators
db.Bookings.find({init_fuel:{$gte: 52, $lte:53}, distance: 870}).count()

-- there is a difference between or and in (generally they are the same)
-- in is on just one attribute but or can be on different attributes
db.Bookings.find({distance: {$in: [870, 3921]}}).count()
db.Bookings.find({$or: [{distance: 2005}, {vendor: "enjoy"}]}).count()


--Logical Operators
db.Bookings.find({city: {$not:{$eq: "Torino"}}})

db.Bookings.find({$and:[{$or: [{distance: {$gte: 1000000}},{distance:{$lte: 0} }]}         ,{$or:[{onClick_disabled:true},{init_fuel: {$lt: 1}}] }   ]},{distance: 1, init_fuel:1, _id: 0})



--just item field null and the item null
db.testAlaki.find({item: null})

-- item does not exist not the value
db.testAlaki.find({item:{$exists: false}})

--item exists but the value is null
db.testAlaki.find({item:{$type: 10}})

--Embedded documents order is important
db.inventory.find( { size: { h: 14, w: 21, uom: "cm" } } )

db.inventory.find({"size.uom": "cm"})
db.inventory.find({"size.h":{$lte: 20}})

db.testAlaki.find({item: null})
db.testAlaki.find({item:{$exists: false}})
db.testAlaki.find({item:{$type: 10}})

-- compound filter
-- if one of the inequalities is true it is OK

-- elemMatch: 
-- one of the items should satisfy both the inequalities


db.testCollec.insertMany([
   { item: "journal", qty: 25, tags: ["blank", "red"], dim_cm: [ 14, 21 ] },
   { item: "notebook", qty: 50, tags: ["red", "blank"], dim_cm: [ 14, 21 ] },
   { item: "paper", qty: 100, tags: ["red", "blank", "plain"], dim_cm: [ 14, 21 ] },
   { item: "planner", qty: 75, tags: ["blank", "red"], dim_cm: [ 22.85, 30 ] },
   { item: "postcard", qty: 45, tags: ["blue"], dim_cm: [ 10, 15.25 ] }
]);
db.testCollec.find({tags:{$exists: true}},{ dim_cm: 1, _id: 0, tags: 1, qty: 1}).sort({dim_cm: 1})--???
db.testCollec.find({tags:{$exists: true}},{ dim_cm: 1, _id: 0, tags: 1, qty: 1}).sort({tags: 1})--??
--Documents are sort based on the first field
--oIn case of ties, the second specified field is considered


db.testCollec.updateMany({"gty": {$lt: 50}}, {$set: {"size.uom": 'in', status: 'P'}, $currentDate: {lastModified: true }})

db.testCollec.updateMany({ "qty": { $lt: 50 } },{$set: { "size.uom": "in", status: "P" },$currentDate: { lastModified: true }})


db.testCollec.aggregate([{$group: {_id: "$name", total: {$sum: "$price"}}},{$match: {price:{$gt: 15}}}])
????


db.testCollec.aggregate([{$group: {_id: "$name", total: {$sum: "$price"}}},{$match: {price:{$gt: 15}}}])
db.testCollec.aggregate([{$group: {_id: "$name", total: {$sum: "$price"}}},{$match: {total:{$gt: 15}}}])
db.testCollec.updateMany({"gty": {$gt:50}},{$inc:{gty: 300}})
db.testCollec.updateMany({gty: {$gt:50}},{$inc:{gty: 300}})
db.testCollec.updateMany({gty: {$gt:50}},{$inc:{gty: 300}})
db.testCollec.updateMany({ "qty": { $lt: 50 } },{$set: { "size.uom": "in", status: "P" },$currentDate: { lastModified: true }})
db.testCollec.updateMany({"gty": {$lt: 50}}, {$set: {"size.uom": 'in', status: 'P'}, $currentDate: {lastModified: true }})
db.testCollec.updateMany({"gty": {$lt: 50}}, {$set: {"size.uom": 'in', status: 'P'}})
$set: { "size.uom": "in", status: "P" },
$currentDate: { lastModified: true }
db.testCollec.updateMany({qty: {$lt: 50}},{$set: {item: "notChanged"})
db.testCollec.updateMany({qty: {$lt: 50}},{item: "notChanged"})
db.testCollec.updateMany({qty:{$lte: 50}},{$set:{item: 'chnaged'}})
db.testCollec.updateMany({gty: {$lt:50}},{$set:{item: "changed"}})
db.testCollec.find({gty:{$exists: true}},{gty: 1, _id: 0})
