use proconio::input;
fn main() {
    input!{n:u32}
    
    let mut cnt = 0;
    for i in 1..{
        cnt += i;
        if cnt >= n{
            println!("{}",i);
            break
        }
    }
    
}