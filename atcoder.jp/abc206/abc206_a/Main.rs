use proconio::input;
fn main() {
    input!{n:u32}
    let n = n*108/100;
    if n<206{
        let ans = "Yay!";
        println!("{}", ans);
    }else if n==206{
        let ans = "so-so";
        println!("{}", ans);
    }else{
        let ans = ":(";
        println!("{}", ans);
    }
}