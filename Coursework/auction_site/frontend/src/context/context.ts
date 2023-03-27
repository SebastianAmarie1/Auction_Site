
const URL = "http://127.0.0.1:8000"

type User = {
    city: string,
    dob: Date,
    email: string,
    first_name: string,
    id: number,
    last_name: string,
    password: string,
    profile_picture: number,
    username: string,
    Message: string,
};

type Product = {
    id: number,
    name: string,
    owner: User,
    description: string,
    starting_price: number,
    start_date: Date,
    finish_date: Date,
    picture: File,
    sold: Boolean,
    
}

type Review = {
    message: string,
    sender: User,
    item: Product,
    date_posted: Date,

}

type Reply = {
    replying: Review,
    message: string,
    item: Product,
    sender: User,
    date_posted: Date,
}

type Bid = {
    user: User,
    product: Product,
    amount: number,
    date_posted: Date,
}
export type {
User,
Product,
Review,
Reply,
Bid,
}
export {URL}