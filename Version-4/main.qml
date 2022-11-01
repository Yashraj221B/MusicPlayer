import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.12

Window {
    id: window
    width: 640
    height: 480
    opacity: 1
    minimumHeight: 300
    minimumWidth: 300
    visible: true
    color: "#00000000"
    title: qsTr("Hello World")

    flags: Qt.FramelessWindowHint | Qt.Window

    property int windowStatus: 0
    property int windowMargin: 10
    property bool visibility: true
    property string btnColorDefault: "#333944"
    property string btnColorMouseOver: "#636e83"
    property string btnColorClicked: "#3077e8"

    QtObject{
        id:app
        function showMinimize(){
            window.showMinimized()
        }
        function maximizeRestore(){
            if (windowStatus == 1){
                windowStatus = 0
                windowMargin = 10
                visibility= true
                window.showNormal()
            }else{
                windowStatus = 1
                windowMargin = 0
                visibility = false
                window.showMaximized()
            }
        }
        function ifMaximizedWindowRestore(){
            if(windowStatus == 1){
                windowStatus = 0
                windowMargin = 10
                visibility = true
            }
        }
        function animrun(){
            if(leftBar.width == 65){
                animation.from = 65
                animation.to = 200
            }else{
                animation.from = 200
                animation.to = 65
            }
            animation.start()
        }
    }

    DropShadow{
        anchors.fill: application
        horizontalOffset: 0
        verticalOffset: 0
        radius: 10
        samples: 16
        color: "#000000"
        source: application
        transparentBorder: true
        z: 0
    }

    MouseArea {
        id: leftEdge
        visible: visibility
        width: 10
        anchors.left: parent.left
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.leftMargin: 0
        anchors.bottomMargin: 10
        anchors.topMargin: 10
        cursorShape: Qt.SizeHorCursor

        DragHandler{
            target: null
            dragThreshold: 0
            onActiveChanged: if (active){window.startSystemResize(Qt.LeftEdge)}
        }
    }

    MouseArea {
        id: topEdge
        visible: visibility
        height: 8
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.rightMargin: 10
        anchors.leftMargin: 10
        anchors.topMargin: 0
        cursorShape: Qt.SizeVerCursor

        DragHandler{
            target: null
            dragThreshold: 0
            onActiveChanged: if (active){window.startSystemResize(Qt.TopEdge)}
        }
    }

    MouseArea {
        id: bottomEdge
        visible: visibility
        height: 10
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        anchors.rightMargin: 10
        anchors.leftMargin: 10
        anchors.bottomMargin: 0
        cursorShape: Qt.SizeVerCursor

        DragHandler{
            target: null
            dragThreshold: 0
            onActiveChanged: if (active){window.startSystemResize(Qt.BottomEdge)}
        }
    }

    MouseArea {
        id: rightEdge
        visible: visibility
        width: 10
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 10
        anchors.topMargin: 10
        anchors.rightMargin: 0
        cursorShape: Qt.SizeHorCursor

        DragHandler{
            target: null
            dragThreshold: 0
            onActiveChanged: if (active){window.startSystemResize(Qt.RightEdge)}
        }
    }

    MouseArea {
        id: topLeft
        visible: visibility
        width: 15
        height: 15
        anchors.left: parent.left
        anchors.top: parent.top
        anchors.leftMargin: 0
        anchors.topMargin: 0
        cursorShape: Qt.SizeFDiagCursor

        DragHandler{
            target: null
            dragThreshold: 0
            onActiveChanged: if(active){window.startSystemResize(Qt.TopEdge | Qt.LeftEdge)}
        }
    }

    MouseArea {
        id: topRight
        visible: visibility
        width: 12
        height: 12
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.topMargin: 0
        anchors.rightMargin: 0
        cursorShape: Qt.SizeBDiagCursor

        DragHandler{
            target: null
            dragThreshold: 0
            onActiveChanged: if(active){window.startSystemResize(Qt.TopEdge | Qt.RightEdge)}
        }
    }

    MouseArea {
        id: bottomLeft
        visible: visibility
        width: 15
        height: 15
        anchors.left: parent.left
        anchors.bottom: parent.bottom
        anchors.leftMargin: 0
        anchors.bottomMargin: 0
        cursorShape: Qt.SizeBDiagCursor

        DragHandler{
            target: null
            dragThreshold: 0
            onActiveChanged: if(active){window.startSystemResize(Qt.BottomEdge | Qt.LeftEdge)}
        }
    }

    MouseArea {
        id: bottomRight
        visible: visibility
        width: 15
        height: 15
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 0
        anchors.rightMargin: 0
        cursorShape: Qt.SizeFDiagCursor

        DragHandler{
            target: null
            dragThreshold: 0
            onActiveChanged: if(active){window.startSystemResize(Qt.BottomEdge | Qt.RightEdge)}
        }
    }

    Rectangle {
        id: application
        visible: true
        color: "#47505f"
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        clip: false
        anchors.rightMargin: windowMargin
        anchors.leftMargin: windowMargin
        anchors.bottomMargin: windowMargin
        anchors.topMargin: windowMargin
        radius: 0


        Rectangle {
            id: topBar
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.rightMargin: 0
            anchors.topMargin: 0
            height: 60
            visible: true
            color: "#333944"

            Button {
                id: menuButton
                x: 0
                y: 0
                width: 65
                anchors.left: parent.left
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                enabled: true
                anchors.leftMargin: 0
                anchors.bottomMargin: 0
                anchors.topMargin: 0
                onClicked: app.animrun()
                //if(animation.running){animation.restart()}else{animation.start()}
                QtObject{
                    id: internal3
                    property var color : if(menuButton.down){
                                             menuButton.down ? btnColorClicked : btnColorDefault
                                         } else {
                                             menuButton.hovered ? btnColorMouseOver : btnColorDefault
                                         }
                }

                background: Rectangle{
                    color: internal3.color


                    Image {
                        width: 20
                        height: 15
                        anchors.verticalCenter: parent.verticalCenter
                        source: "Assets/Light/menu.png"
                        anchors.verticalCenterOffset: 2
                        anchors.horizontalCenter: parent.horizontalCenter
                    }
                }
            }

            Rectangle {
                id: appNav
                x: 517
                width: 105
                height: 30
                color: "#00000000"
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.bottom: descr.top
                anchors.rightMargin: 0
                anchors.bottomMargin: 0
                anchors.topMargin: 0

                Button {
                    id: minimize
                    width: 35
                    onClicked: app.showMinimize()
                    anchors.left: parent.left
                    anchors.top: parent.top
                    anchors.bottom: parent.bottom
                    anchors.topMargin: 0
                    anchors.bottomMargin: 0
                    anchors.leftMargin: 0
                    focus: true

                    QtObject{
                        id: internal
                        property string color : if(minimize.down){
                                                    minimize.down ? btnColorClicked : btnColorDefault
                                                } else {
                                                    minimize.hovered ? btnColorMouseOver : btnColorDefault
                                                }
                    }

                    background: Rectangle{
                        color: internal.color

                        Image {
                            id: iconBtn
                            source: "Assets/Light/minimize.png"
                            anchors.verticalCenter: parent.verticalCenter
                            anchors.horizontalCenter: parent.horizontalCenter
                            height: 16
                            width: 16
                        }
                    }
                }
                Button {
                    id: maximize
                    width: 35
                    anchors.left: minimize.right
                    anchors.top: parent.top
                    anchors.bottom: parent.bottom
                    anchors.topMargin: 0
                    anchors.bottomMargin: 0
                    anchors.leftMargin: 0
                    onClicked: app.maximizeRestore()

                    QtObject{
                        id: internal1
                        property string color : if(maximize.down){
                                                    maximize.down ? btnColorClicked : btnColorDefault
                                                } else {
                                                    maximize.hovered ? btnColorMouseOver : btnColorDefault
                                                }
                    }

                    background: Rectangle{
                        color: internal1.color

                        Image {
                            id: iconBtn1
                            source: "Assets/Light/maximize.png"
                            anchors.verticalCenter: parent.verticalCenter
                            anchors.horizontalCenter: parent.horizontalCenter
                            height: 16
                            width: 16
                        }
                    }
                }
                Button {
                    id: close
                    width: 35
                    anchors.left: maximize.right
                    anchors.right: parent.right
                    anchors.top: parent.top
                    anchors.bottom: parent.bottom
                    anchors.leftMargin: 0
                    onClicked: window.close()

                    QtObject{
                        id: internal2
                        property string color : if(close.down){
                                                    close.down ? "#ff0062" : btnColorDefault
                                                } else {
                                                    close.hovered ? btnColorMouseOver : btnColorDefault
                                                }
                    }

                    background: Rectangle{
                        color: internal2.color

                        Image {
                            id: iconBtn2
                            source: "Assets/Light/close.png"
                            anchors.verticalCenter: parent.verticalCenter
                            anchors.horizontalCenter: parent.horizontalCenter
                            height: 16
                            width: 16
                        }
                    }
                }
            }

            Rectangle {
                id: descr
                y: 31
                height: 25
                color: "#374456"
                anchors.left: menuButton.right
                anchors.right: parent.right
                anchors.bottom: parent.bottom
                anchors.bottomMargin: 0
                anchors.leftMargin: 0
                anchors.rightMargin: 0
            }

            Rectangle {
                id: titleBar
                color: "#00000000"
                anchors.left: menuButton.right
                anchors.right: appNav.left
                anchors.top: parent.top
                anchors.bottom: descr.top
                anchors.bottomMargin: 0
                anchors.rightMargin: 0
                anchors.leftMargin: 0

                DragHandler{
                    dragThreshold: 0
                    onActiveChanged: if(active){window.startSystemMove();app.ifMaximizedWindowRestore()}
                }

                Text {
                    id: text1
                    width: 154
                    color: "#ffffff"
                    text: qsTr("My Application")
                    anchors.left: parent.left
                    anchors.top: parent.top
                    anchors.bottom: parent.bottom
                    font.pixelSize: 16
                    verticalAlignment: Text.AlignVCenter
                    anchors.leftMargin: 10
                    anchors.bottomMargin: 0
                    anchors.topMargin: 0
                }
            }

        }



        Rectangle {
            id: leftBar
            width: 65
            height: 45
            color: "#333944"
            anchors.left: parent.left
            anchors.top: topBar.bottom
            anchors.bottom: parent.bottom
            anchors.leftMargin: 0
            anchors.bottomMargin: 0
            anchors.topMargin: 0


            PropertyAnimation {
                id: animation
                target: leftBar
                property: "width"
                duration: 200
                easing.type: Easing.InOutQuint
            }

            Button {
                id: homeButton
                width: leftBar.width
                height: 60
                text: qsTr("Home")
                anchors.left: parent.left
                anchors.top: parent.top
                anchors.leftMargin: 0
                anchors.topMargin: 0

                background: Rectangle{
                    id: rectangle
                    color: if(homeButton.down){
                               homeButton.down ? btnColorClicked : btnColorDefault
                           } else {
                               homeButton.hovered ? btnColorMouseOver : btnColorDefault
                           }

                    Rectangle{
                        width: 4
                        color: "#0f59c8"
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        anchors.bottomMargin: 0
                        anchors.topMargin: 0
                    }
                    Rectangle{
                        width:4
                        color: "#47505f"
                        anchors.right: parent.right
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        anchors.rightMargin: 0
                    }
                }
                contentItem: Item {
                    id: name
                    anchors.fill: parent
                    Text {
                        id: auto
                        y: 13
                        width: 49
                        height: 23
                        color: "#ffffff"
                        text: homeButton.text
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: icon.right
                        anchors.verticalCenterOffset: 2
                        anchors.leftMargin: 20
                        font.capitalization: Font.MixedCase
                        font.pointSize: 14
                    }
                    Image {
                        id: icon
                        y: 0
                        width: 20
                        height: 20
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: parent.left
                        source: "Assets/Light/home.png"
                        anchors.leftMargin: 24
                    }
                }
            }

            Button {
                id: settings
                y: 60
                width: leftBar.width
                height: 60
                text: qsTr("Settings")
                anchors.left: parent.left
                anchors.bottom: parent.bottom
                anchors.leftMargin: 0
                anchors.bottomMargin: 0
                background: Rectangle {
                    id: rectangle1
                    color: if(settings.down){
                               settings.down ? btnColorClicked : btnColorDefault
                           } else {
                               settings.hovered ? btnColorMouseOver : btnColorDefault
                           }
                    Rectangle {
                        width: 4
                        color: "#0f59c8"
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        anchors.bottomMargin: 0
                        anchors.topMargin: 0
                        visible: false
                    }

                    Rectangle {
                        width: 4
                        visible: false
                        color: "#47505f"
                        anchors.right: parent.right
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        anchors.rightMargin: 0
                    }
                }
                contentItem: Item {
                    id: name1
                    anchors.fill: parent
                    Text {
                        id: auto1
                        y: 13
                        width: 49
                        height: 23
                        color: "#ffffff"
                        text: settings.text
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: icon1.right
                        anchors.leftMargin: 24
                        font.capitalization: Font.MixedCase
                        font.pointSize: 14
                        anchors.verticalCenterOffset: 2
                    }

                    Image {
                        id: icon1
                        y: 0
                        width: 20
                        height: 20
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: parent.left
                        source: "Assets/Light/settings.png"
                        anchors.leftMargin: 24
                    }
                }
            }
        }
        Rectangle {
            id: content
            visible: true
            color: "#47505f"
            anchors.left: leftBar.right
            anchors.right: parent.right
            anchors.top: topBar.bottom
            anchors.bottom: parent.bottom
            anchors.leftMargin: 0
            anchors.topMargin: 0
        }
    }
}
