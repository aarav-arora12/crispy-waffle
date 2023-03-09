import cv2


img = cv2.imread("solar-system.jpg")

cv2.imshow("Display Image",img)

cv2.waitKey(0)


cv2.putText(img,
            "Sun",
            (30,50),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (0,0,255)
            )

cv2.putText(img,
            "Mercury",
            (100,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Venus",
            (200,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Earth",
            (300,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Mars",
            (400,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Jupiter",
            (500,350),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Saturn",
            (700,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Uranus",
            (1000,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Neptun",
            (1100,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )


cv2.imshow("output",img)
cv2.imwrite("Solar_systemwithname.jpg",img)


cv2.waitKey(0)