use proconio::input;
use std::collections::BTreeMap;

fn main() {
    input!{
        n:usize,
        a:[i32;n]}
    
    let mut cnt = BTreeMap::new();
    for i in a {
        *cnt.entry(i).or_insert(0usize) += 1;
    }
    let mut ans = 0;
    for (i,j) in cnt{
        ans  += j*(n-j);
    }
    println!("{}",ans/2);
    
}