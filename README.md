# Crawling_GPU_Info
Bài toán: Sau khi bitcoin và các đồng tiền ảo sụt giảm, công ty có nhu cầu khảo sát thông tin về card đồ họa thông qua một website. Yêu cầu team Data Engineer collect và thống kê các thông tin tại danh mục trên website: [https://www.newegg.com](https://www.newegg.com/GPUs-Video-Graphics-Cards/SubCategory/ID-48?Tid=7709) để phía đội kinh doanh có cơ sở triển khai chiến dịch mới.

Mô tả cụ thể:

- Nguồn dữ liệu cần crawl là danh mục sau: [https://www.newegg.com/GPUs-Video-Graphics-Cards/SubCategory/ID-48?Tid=7709](https://www.newegg.com/GPUs-Video-Graphics-Cards/SubCategory/ID-48?Tid=7709)
- Thông tin cần lấy:
    - Title
    - Branding (Hãng)
    - Rating
    - Price (Current Price)
    - Shipping (Free, Ko ship, hay mất phí)
    - Image URL
- Số lượng: Toàn bộ các sản phẩm của 100 pages (khoảng hơn 3000 sản phẩm)
- Thông tin sau khi collect đẩy vào một cơ sở dữ liệu để sử dụng về sau (MYSQL)
- Yêu cầu thống kê (visualize dữ liệu nếu có thể):
    - Các hãng đang cung cấp Card đồ họa, số lượng sản phẩm của mỗi hãng.
    - Phân bố giá của các sản phẩm (Mức giá phổ biến là bao nhiêu)
    - Phân bố giá sản phẩm theo hãng
    - Biểu diễn mối liên hệ giữa giá sản phẩm và rating của người dùng
    - Top 10 các sản phẩm được mua nhiều nhất và có rating cao nhất
