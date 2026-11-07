#!/usr/bin/env python3
import random #rastgele sayılar için bu kütüphaneyi ekledik.
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32 #32 bitlik tam sayıları ifade eder ve bu sayıları kod içerisinde kullanbilmemizi sağlar.
from rclpy.qos import QoSProfile, ReliabilityPolicy, DurabilityPolicy

class NumberPublisherNode(Node):

    def __init__(self):
        super().__init__("number_publisher")
        self.get_logger().info("Number publisher has been started.")

        qos_profile = QoSProfile(
            depth = 10, #mesaj geçmişi için en fazla 10 mesajlık bir kuyruk tutulur.
        reliability = ReliabilityPolicy.RELIABLE, #güvenilir  bir şekilde mesajların iletilmesini sağlar.
        durability= DurabilityPolicy.TRANSIENT_LOCAL #yeni abone olanlara saklanan mesaj geçmişini sunar.
        )

        self.publisher_ = self.create_publisher(#number isimli bir yayımcı oluşturmak istediğimizi belirtmek için bu kodu yazıyoruz.
            Int32,#Int32 göndereceğimiz mesajın veri türünü belirtir.
            '/number',#mesajı göndereceğimiz topic in ismidir.
            qos_profile #deminki qos ayarlarını kullanmak için ekledik.
        )
        self.timer = self.create_timer(0.5,self.publish_number) #saniyede 2 kez yayın yapabilmemiz için kullandık 2Hz yayın aralığı yani.

    def publish_number(self):
        msg = Int32()
        msg.data = random.randint(1,1000)

        self.publisher_.publish(msg)

        #self.publisher_ burada yayıncı nesnemiz
        #publish() burada mesajı yayımlayan fonksiyon
        #msg ise göndereceğimiz mesajdır.

        self.get_logger().info(f'Publishing: {msg.data}') #burası yayınladığımız sayıyı terminalde gösterecek olan satır.


def main(args=None):
    rclpy.init(args=args)
    node =  NumberPublisherNode()
    try:
        rclpy.spin(node) #node u çalıştırmayı deneer.
    except KeyboardInterrupt: #programın kontrolsüz şekilde sonlanmasını önler.
        pass
    finally: 
        node.destroy_node() #node u kapatır ve kaynakları temizler.
        rclpy.shutdown()
                    
if __name__ == '__main__':
    main()