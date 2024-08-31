public class Main {
    public static void main(String[] args) {
        ShapeFactory shapeFactory = new ShapeFactory();

        Shape circle = shapeFactory.createCircle();
        System.out.println(circle.draw());

        Shape square = shapeFactory.createSquare();
        System.out.println(square.draw());

        Shape rectangle = shapeFactory.createRectangle();
        System.out.println(rectangle.draw());
    }
}